#!/usr/bin/env python2.7
#file: assign_scores.py

from __future__ import division
import sys
import os

#your_djangoproject_home="/home/djrh/Programming/AHS-Freshman-Debates"
#sys.path.append(your_djangoproject_home)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#import logging
from   debates.models import Score, Team
from io import open

#logger = logging.getLogger('logview.debugger')
# Full path to your django project directory

def scoresToFile():
    scores = list(Score.objects.all())
    teams  = list(Team.objects.all())
    for t in teams:
        judge_scores = list([s for s in scores if s.team_number == t.team_number])
        avg_score = averageScores(judge_scores)
        writeScoreToFile(t.team_number, avg_score)

def writeScoreToFile(team_number, score):
    f = open(u"scores.txt", u"a")
    #TODO, do as a template?
    score_format = u"""
                   Team {0} got an overall argument score of {1}.\n
                   \tThe first speaker's score was:   {2}.
                   \tThe second speaker's score was:  {3}.
                   \tThe slideshow score was:         {4}.
                   \tThe rebuttal score was:          {5}.
                   \tThe cross examination score was: {6}.
                   \tThe argument score was:          {7}.
                   """
    score_string = score_format.format(unicode(team_number),
                                       unicode(score.argument),
                                       unicode(score.speaker1),
                                       unicode(score.speaker2),
                                       unicode(score.slideshow),
                                       unicode(score.rebuttal),
                                       unicode(score.cross_examination),
                                       unicode(score.argument))
    f.write(score_string)
    f.close()

#[Score] -> Score
def averageScores(scores):
    if len(scores) == 0:
        return None
    #TODO, rewrite to use a dictionary and generically average terms
    total_rebuttal          = 0
    total_speaker1          = 0
    total_speaker2          = 0
    total_slideshow         = 0
    total_cross_examination = 0
    total_argument          = 0
    for s in scores:
        total_speaker1          += float(s.speaker1)
        total_speaker2          += float(s.speaker1)
        total_slideshow         += float(s.slideshow)
        total_rebuttal          += float(s.rebuttal)
        total_cross_examination += float(s.cross_examination)
        total_argument          += float(s.argument)
    avg_score                   = Score()
    avg_score.speaker1          = total_speaker1          / len(scores)
    avg_score.speaker2          = total_speaker2          / len(scores)
    avg_score.slideshow         = total_slideshow         / len(scores)
    avg_score.rebuttal          = total_rebuttal          / len(scores)
    avg_score.cross_examination = total_cross_examination / len(scores)
    avg_score.argument          = total_argument          / len(scores)
    return avg_score
