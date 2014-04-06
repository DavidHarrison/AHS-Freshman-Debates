from   django.shortcuts               import render
from   debates.models                 import (
                                                 Topic, Location, Date, User,
                                                 Score, GoogleUser, Student,
                                                 Team
                                             )
from   debates.forms                  import (
                                                 ScoreForm,
                                                 RegistrationForm,
                                                 ImportExcelForm
                                             )
from   freshmandebates.assign_scores  import averageScores
from   django.shortcuts               import render_to_response
from   django.http                    import (
                                                 HttpResponseRedirect,
                                                 HttpResponse,
                                                 HttpResponseServerError
                                             )
from   django.contrib.auth.decorators import (
                                                 login_required,
                                                 user_passes_test
                                             )
from   django.contrib.auth.models     import User
from   django.forms.extras.widgets    import SelectDateWidget
import datetime
from   django.utils.timezone          import utc
import logging

logger = logging.getLogger('logview.debugger')

# get the debate that are on
def judge(request):
    aff_form = ScoreForm()
    neg_form = ScoreForm()
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            s = form.save()
            #if the form is affirmative, set the object to be affirmative
            if 'form_affirmative' in request.POST:
                s.is_aff = True
                aff_form = form
            #else, assume its negative (not affirmative)
            else:
                s.is_aff = False
                neg_form = form
            #save the form to the database
            s.save()
    forms = {
                'affirmative_form': aff_form,
                'negative_form':    neg_form
            }
    return render(request,'debates/judge.html', forms)

def new_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user              = GoogleUser()
            user.first_name   = form.cleaned_data.get('first_name')
            logger.debug(user.first_name)
            user.last_name    = form.cleaned_data.get('last_name')
            logger.debug(user.last_name)
            user.email        = form.cleaned_data.get('email')
            user.role         = form.cleaned_data.get('role')
            user.password     = form.cleaned_data.get('password')
            user.is_admin     = False
            user.is_staff     = True
            user.is_superuser = False
            user.save()
            user.create_user(user.first_name, user.last_name, user.email,
                             user.password)
    else:
        form = RegistrationForm()
    return render(request, 'debates/new_user.html', {'Form': form,})

def handle(request):
    aff_scores = Affirmative.objects.all()
    aff_scores = Negative.objects.all()
    return render(request,'debates/scoring_upload.html',
                  {
                      'affirmative_scores': aff_scores,
                      'negative_scores':    neg_scores,
                  })

def splash(request):
    return render(request,'debates/splash.html')

def teacher(request):
    #testing it out
    tn = 5
    judge_scores = Score.objects.filter(team_number = tn)
    avg_score = averageScores(judge_scores)
    return render(request,'debates/teacher.html', {'score': avg_score})

def teacherselector(request):
    return render(request,'debates/teacher_selector.html')

def teamcreate(request):
    Submit_form = 'null'
    new_team = Team()
    return render(request,'debates/team_create.html')

def debateselector(request):
    return render(request,'debates/debate_selector.html')

def test_flowcell(request):
    # If the form has been submitted...
    if request.method == 'POST':
        # A form bound to the POST data
        form = ImportExcelForm(request.POST, request.FILES)
        # All validation rules pass
        if form.is_valid():
            parser = ExcelParser()
            success, log = parser.read_excel(request.FILES['file'] )
            if success:
                # redirects to aliquot page ordered by the most recent
                return redirect(reverse('admin:index')
                                + "pages/flowcell_good/")
            else:
                errors = '* Problem with flowcell * <br><br>log details below:<br>' + "<br>".join(log)
    else:
        # An unbound form
        form = ImportExcelForm()
    return render(request,'debates/file_upload.html',{'form': form})

#def CSVUpload(request):
#    if request.method == 'POST':
#        form = MyForm(request.POST, request.FILES)
#        if form.is_valid():
#            uploaded_file = request.FILES['html-file-attribute-name']
#            # Write the file to disk
#            fout = open("path/to/save/file/to/%s" % uploaded_file.name, 'wb')
#            for chunk in uploaded_file.chunks():
#                fout.write(chunk)
#            fout.close()
#            
#        else:
#             form = codeUploadForm()
#             context = {'form': form}
#             return render_to_response('import.html', context,
#                                       context_instance=RequestContext(
#                                           request))
#    return render(request,{})
