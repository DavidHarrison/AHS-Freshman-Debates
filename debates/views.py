#!/usr/bin/env python3.4
#file: views.py

from debates.models import Topic, Location, Date, Score, GoogleUser, Debater, Team
from debates.forms import ScoreForm, TeamForm, RegistrationForm
from debates.assign_scores import averageScores
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
#from social.backends.google import GooglePlusAuth
from django.conf import settings
from logging import getLogger

logger = getLogger('logview.debugger')

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
    return render_to_response('debates/splash.html', {
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)
    }, RequestContext(request))

#def splash(request):
#    return render_to_response('debates/splash.html', {}, RequestContext(request))

#TODO, add team selector and filter teams by teacher
def view_scores(request):
    #testing it out
    tn = 5
    team = Team.objects.filter(team_number = tn)
    judge_scores = Score.objects.filter(team_number = tn)
    avg_score = averageScores(judge_scores)
    return render(request, 'debates/view_scores.html', {'team':  team,
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
    debaters = list(Debater.objects.all())
    topics   = list(Topic.objects.all())
    context = {
                  'form': form,
                  'topics': topics,
                  'debaters': debaters
              }
    return render(request, 'debates/team_create.html', context)

#TODO, fill out
def debate_selector(request):
    return render(request, 'debates/debate_selector.html')
