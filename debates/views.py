#!/usr/bin/env python3.4
#file: views.py

from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.shortcuts import redirect, render, render_to_response
from django.template import RequestContext
from django.conf import settings
from logging import getLogger

from social.backends.google import GooglePlusAuth

#logger = getLogger('logview.debugger')

def login(request):
    if request.user.is_authenticated():
        if request.user.groups.filter(name='admins').count():
            return redirect('/admin')
        if request.user.groups.filter(name='teachers').count():
            return redirect('/teacher')
        if request.user.groups.filter(name='judges').count():
            return redirect('/judge')
        if request.user.groups.filter(name='debaters').count():
            return redirect('/debater')
    return render_to_response('debates/login.html', {
               'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None)
           }, RequestContext(request))

#menu for a teacher, shows teams
#@user_passes_test(lambda u: u.groups.all().filter(name='teachers').count(), login_url='/')
def teacher(request):
    #TODO, is all this necessary
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render_to_response('debates/teacher.html', {
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope
    }, RequestContext(request))

#(teacher) view details on a team
#@permission_required('debates.view_team', login_url='/')
def view_team(request):
    return

#menu for a judge, shows all debates that they have to score
#@user_passes_test(lambda u: u.groups.all().filter(name='judges').count(), login_url='/')
def judge(request):
    #TODO, is all this necessary
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render_to_response('debates/judge.html', {
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope
    }, RequestContext(request))


#(judge) submit scores for a debate
#@permission_required('debates.score_debate', login_url='/')
def score_debate(request):
    return

#menu for a debater shows any relevant imformation (scores, debate details etc.)
#@user_passes_test(lambda u: u.groups.all().filter(name='debaters').count(), login_url='/')
def debater(request):
    #TODO, is all this necessary
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render_to_response('debates/debater.html', {
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope
    }, RequestContext(request))


#(debater, teacher) view score for a debate
#@permission_required('debates.view_score', login_url='/')
def view_score(request):
    return
