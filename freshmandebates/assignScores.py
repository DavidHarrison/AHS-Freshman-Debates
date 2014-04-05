#!/usr/bin/env python2.7
#file: assignScores.py

#import logging
import sys
import os
from   debates.models import Student, GoogleUser, OverallScore, Team

#logger = logging.getLogger('logview.debugger')
# Full path and name to your csv file
csv_filepathname="/AHS-Freshmen-Debates/freshmendebates/freshmen.csv"
# Full path to your django project directory
your_djangoproject_home="/AHS-Freshmen-Debates/freshmendebates/freshmendebates/"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

affirmative_list  = list(filter(lambda s: s.isAff(), OverallScore.objects.all()))
negative_list     = list(filter(lambda s: s.isAff(), OverallScore.objects.all()))
team_list         = list(Team.objects.all())

for team in team_list:
    team_number = team.team_number
    # TODO, are team numbers unique, or do both sides have the same number
    # if they are unique, aff/neg filtering can be removed
    if team.affirmative:
        score_list = list(filter(lambda s: s.TeamNumber == team_number,
                                 affirmative_list))
    else:
        score_list = list(filter(lambda s: s.TeamNumber == team_number,
                                 negative_list))

    total_rebuttal  = 0
    total_speaker1  = 0
    total_speaker2  = 0
    total_slideshow = 0
    #total_cross_examination = 0
    total_argument  = 0
    
    for score in score_list:
        total_speaker1  += float(score.Speaker1)
        total_speaker2  += float(score.Speaker1)
        total_slideshow += float(score.SlideShowScore)
        total_rebuttal  += float(score.Rebuttal)
        total_argument  += float(score.Argument)

    avg_speaker1  = total_speaker1  / len(score_list)
    avg_speaker2  = total_speaker2  / len(score_list)
    avg_slideshow = total_slideshow / len(score_list)
    avg_rebuttal  = total_rebuttal  / len(score_list)
    avg_argument  = total_argument  / len(score_list)
   
    f = open("scores.txt", "a")
    #do as a template?
    score_format = """
                   Team {0} got an overall argument score of {1}.\n
                   \tThe first speaker's score was:  {2}.
                   \tThe second speaker's score was: {3}.
                   \tThe slideshow score was:        {4}.
                   \tThe rebuttal score was:         {5}.
                   \tThe argument score was:         {6}.
                   """
    score_string = score_format.format(str(team_number),
                                       str(avg_argument),
                                       str(avg_speaker1),
                                       str(avg_speaker2),
                                       str(avg_slideshow),
                                       str(avg_rebuttal),
                                       str(avg_argument))
    f.write(score_string)
    f.close()
