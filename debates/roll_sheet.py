#!/usr/bin/env python3.4

import logging
import sys
import os
#from   django.forms.extras.widgets import SelectDateWidget
#import datetime
#from   django.db                   import models
from   debates.models              import Debate, Team, Period
#from   django.utils                import timezone

#logger = logging.getLogger('logview.debugger')

#your_djangoproject_home="/AHS-Freshmen-Debates/freshmendebates/freshmendebates/"
#sys.path.append(your_djangoproject_home)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

f = open('roll_sheet', 'w')

all_periods = []
all_periods = Period.objects.all()

logger.debug(len(all_periods))
number_of_periods = len(all_periods)
#sort periods
for x in range(0,number_of_periods):
    period = all_periods[x]
    period = period.period
    logger.debug("Period is " + period)
    #get debates for this period
    debates_for_period = []
    debates_for_period = Debate.objects.filter(period = period)
    logger.debug(debates_for_period[0])
    number_of_debates = len(debates_for_period)
    for x in range(0,number_of_debates):
        current_debate = debates_for_period[0]
        location = current_debate.location
        affirmative_team = current_debate.affirmative
        negative_team = current_debate.negative
        spectators = []
        spectators = current_debate.spectators
        number_of_spectators = len(spectators)
        f.write('Period: ' + period + ' Location: ' + location)
        f.write('Teams debating: ' + affirmative + ', ' + negative)
        f.write('Spectator Teams:')
        for x in range(0,number_of_spectators):
            if x == number_of_spectators:
                f.write(' ' + spectators[x].team_Number)
            else:
                f.write(' ' + spectators[x].team_Number + ',')
