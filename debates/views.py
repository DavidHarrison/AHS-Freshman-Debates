#!/usr/bin/env python3.4
#file: views.py

from   django.shortcuts       import render
from   debates.models         import (
                                         Topic, Location, Date, Score,
                                         GoogleUser, Student, Team
                                     )
from   debates.forms          import (
                                         ScoreForm, TeamForm,
                                         RegistrationForm, UploadFileForm
                                     )
from   debates.assign_scores  import averageScores
from   debates.load           import parseDebaters
from   django.shortcuts       import render_to_response
from   django.template        import RequestContext
import logging

logger = logging.getLogger('logview.debugger')

# get the debate that are on
def judge(request):
    aff_form = ScoreForm()
    neg_form = ScoreForm()
    #TODO, what should happen with this
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
    return render(request, 'debates/judge.html', forms)

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

#TODO, what needs to happen with this?
def scoring_upload(request):
    aff_scores = Score.objects.filter(is_aff = True)
    neg_scores = Score.objects.filter(is_aff = False)
    return render(request, 'debates/scoring_upload.html',
                  {
                      'affirmative_scores': aff_scores,
                      'negative_scores':    neg_scores,
                  })

def splash(request):
    return render_to_response('debates/splash.html', RequestContext(request))

def teacher(request):
    #testing it out
    tn = 5
    team = Team.objects.filter(team_number = tn)
    judge_scores = Score.objects.filter(team_number = tn)
    avg_score = averageScores(judge_scores)
    return render(request, 'debates/teacher.html', {'team':  team,
                                                    'score': avg_score})

def teacher_selector(request):
    return render(request, 'debates/teacher_selector.html')

def team_create(request):
    form = TeamForm()
    #TODO, what should happen with this
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        form = TeamForm(request.POST)
        #TODO, what should happen if this fails?
        if form.is_valid():
            s = form.save()
            logger.debug(s.team_number)
            s.save()
    debaters = list(Student.objects.all())
    topics   = list(Topic.objects.all())
    context = {
                  'form': form,
                  'topics': topics,
                  'debaters': debaters
              }
    return render(request, 'debates/team_create.html', context)

def debate_selector(request):
    return render(request, 'debates/debate_selector.html')

def import_debaters(request):
    logger.debug("importing debaters")
    form = UploadFileForm()
    # If the form has been submitted...
    if request.method == 'POST':
        logger.debug("method: POST")
        # A form bound to the POST data
        form = UploadFileForm(request.POST, request.FILES)
        # All validation rules pass
        if form.is_valid():
            logger.debug("form is valid")
            f = form.save()
            debaters = parseDebaters(f.upload_file)
            for d in debaters:
                d.save()
        #TODO, render failure
        else:
            logger.debug("form is invalid")
            logger.debug("file: " + str(form.upload_file))
    return render(request, 'debates/file_upload.html', {'form': form})

'''
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['html-file-attribute-name']
            # Write the file to disk
            #fout = open("path/to/save/file/to/%s" % uploaded_file.name, 'wb')
            #for chunk in uploaded_file.chunks():
            #    fout.write(chunk)
            #fout.close()
        else:
            form = codeUploadForm()
            context = {'form': form}
            return render_to_response('import.html', context,
                                       context_instance=RequestContext(
                                                            request))
    return render(request, 'debates/upload_csv.html')
'''
