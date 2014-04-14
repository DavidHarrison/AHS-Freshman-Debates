#!/usr/bin/env python2.7
#file: views.py

from django.shortcuts       import render
from debates.models         import (
                                       Topic, Location, Date, Score,
                                       GoogleUser, Debater, Team
                                   )
from debates.forms          import ScoreForm, TeamForm, RegistrationForm
from debates.assign_scores  import averageScores
from django.shortcuts       import render_to_response
from django.template        import RequestContext
from logging                import getLogger

logger = getLogger(u'logview.debugger')

# get the debate that are on
def judge(request):
    aff_form = ScoreForm()
    neg_form = ScoreForm()
    #TODO, what should happen with this
    if request.method == u'GET':
        pass
    elif request.method == u'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            s = form.save()
            #if the form is affirmative, set the object to be affirmative
            if u'form_affirmative' in request.POST:
                s.is_aff = True
                aff_form = form
            #else, assume its negative (not affirmative)
            else:
                s.is_aff = False
                neg_form = form
            #save the form to the database
            s.save()
    forms = {
                u'affirmative_form': aff_form,
                u'negative_form':    neg_form
            }
    return render(request, u'debates/judge.html', forms)

#TODO, what needs to happen with this?
def scoring_upload(request):
    aff_scores = Score.objects.filter(is_aff = True)
    neg_scores = Score.objects.filter(is_aff = False)
    return render(request, u'debates/scoring_upload.html',
                  {
                      u'affirmative_scores': aff_scores,
                      u'negative_scores':    neg_scores,
                  })

def splash(request):
    return render_to_response(u'debates/splash.html', RequestContext(request))

#TODO, add team selector and filter teams by teacher
def view_scores(request):
    #testing it out
    tn = 5
    team = Team.objects.filter(team_number = tn)
    judge_scores = Score.objects.filter(team_number = tn)
    avg_score = averageScores(judge_scores)
    return render(request, u'debates/view_scores.html', {u'team':  team,
                                                         u'score': avg_score})

def teacher_selector(request):
    return render(request, u'debates/teacher_selector.html')

def team_create(request):
    form = TeamForm()
    #TODO, what should happen with this
    if request.method == u'GET':
        pass
    elif request.method == u'POST':
        form = TeamForm(request.POST)
        #TODO, what should happen if this fails?
        if form.is_valid():
            s = form.save()
            logger.debug(s.team_number)
            s.save()
    debaters = list(Debater.objects.all())
    topics   = list(Topic.objects.all())
    context = {
                  u'form': form,
                  u'topics': topics,
                  u'debaters': debaters
              }
    return render(request, u'debates/team_create.html', context)

#TODO, fill out
def debate_selector(request):
    return render(request, u'debates/debate_selector.html')
