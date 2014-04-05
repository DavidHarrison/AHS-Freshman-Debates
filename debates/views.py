from   django.shortcuts               import ( render, get_object_or_404 )
from   debates.models                 import (
                                                 Topic, Location, Date, User,
                                                 Form, SubmittedOverallScore,
                                                 GoogleUser, Student
                                             )
from   debates.forms                  import (
                                                 OverallScore,
                                                 RegistrationForm,
                                                 ImportExcelForm
                                             )
from   django.shortcuts               import ( render_to_response )
from   django.http                    import (
                                                 HttpResponseRedirect,
                                                 HttpResponse,
                                                 HttpResponseServerError
                                             )
from   django.contrib.auth.decorators import (
                                                 login_required,
                                                 user_passes_test
                                             )
from   django.contrib.auth.models     import ( User )
from   django.forms.extras.widgets    import ( SelectDateWidget )
import datetime
from   django.utils.timezone          import ( utc )
import logging

logger = logging.getLogger('logview.debugger')

def root(request):
    return render(request,'debates/index.html')

# get the debate that are on
def judge(request):
    #Submit_form = 'null'
    Affform = OverallScore()
    Negform = OverallScore()
    if request.method == 'GET':
        logger.debug('Getting request method GET')
    elif request.method == 'POST':
        logger.debug('Getting request method POST')
        logger.debug(request.POST)
        form = OverallScore(request.POST)
        if form.is_valid():
            #creating an instance of submitted scores to save to database
            p = fillScore(form, SubmittedOverallScore())
            logger.debug('Form has been saved')
            if 'form_Affirmative' in request.POST:
                p.isAff = True
                Affform = form
                #Submit_form = 'aff'
                logger.debug('Form is Positive')
            elif 'form_Negative' in request.POST:
                p.isAff = False
                Negform = form
                #Submit_form = 'neg'
                logger.debug('Form is Negative')
            p.save()
        if request.is_ajax():
            logger.debug('Request is ajax')
            msg = "Operation received correctly"
            logger.debug(msg)
    #msg = "The operation has been received correctly."
    #print request.POST
    #return render_to_response('debates/scoring_upload.html', {'msg':msg},
    #                          context_instance=RequestContext(request))
    #return render_to_response(msg)
    forms = {
                'Affirmative_Form': Affform,
                'Negative_Form':    Negform
            }
    return render(request,'debates/judge.html', forms)

# fill out a given score from a given form
def fillScore(form, score):
    score.Speaker1         = form.cleaned_data.get('Speaker 1')
    score.Speaker2         = form.cleaned_data.get('Speaker 2')
    score.CrossExamination = form.cleaned_data.get('Cross Examination')
    score.SlideShowScore   = form.cleaned_data.get('Slide Show')
    score.Argument         = form.cleaned_data.get('Argument')
    score.Rebuttal         = form.cleaned_data.get('Rebuttal')
    #score.?               = form.cleaned_data.get('Team')
    score.TeamNumber       = ''
    return score


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
    Affirmative_Scores = Affirmative.objects.all()
    Negative_Scores    = Negative.objects.all()
    return render(request,'debates/scoring_upload.html',
                  {
                      'Affirmative_Scores': Affirmative_Scores,
                      'Negative_Scores':    Negative_Scores,
                  })

def splash(request):
    return render(request,'debates/Splash.html', {})

def teacher(request):
    #Index = SubmittedOverallScore.objects.filter(TeamNumber =
    #            'Test, still need to get team numbers')
    Team = get_object_or_404(SubmittedOverallScore)
    return render(request,'debates/Teacher.html', {'Team': Team})

def teacherselector(request):
    return render(request,'debates/TeacherSelector.html', {}) 

def teamcreate(request):
    Submit_form = 'null'
    #TODO, define/find function
    #new_team = Team()
    return render(request,'debates/TeamCreate.html', {})    

def debateselector(request):
    return render(request,'debates/DebateSelector.html', {})

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
    return render(request,'debates/file_upload.html',{'form': form,})

#def CSVUpload(request):
#    if request.method == 'POST':
#        form = MyForm(request.POST, request.FILES)
#        if form.is_valid():
#            uploaded_file = request.FILES['html-file-attribute-name']
#            # Write the file to disk
#            fout = open("path/to/save/file/to/%s" % uploaded_file.name,
#                        'wb')
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
