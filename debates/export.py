#!/usr/bin/env python2.7

from __future__ import with_statement
import logging
import sys
import os
from   debates.models import Debate, Period
from   string         import Template
from io import open
from itertools import imap

logger = logging.getLogger(u'logview.debugger')

ROLL_FILE = u"roll_sheet"
TEMPLATE = Template(u"""
                    Period: $period\n
                    Location: $location\n
                    Teams debating: $aff_teams, $neg_teams\n
                    Spectator teams: $spec_teams\n
                    """)

def writeRoll():
    #clear any existing data from the ROLL_FILE
    open(ROLL_FILE, u'w').close()
    periods = list(imap(lambda p: p.period, Period.object.all()))
    logger.debug(u"Num periods: " + unicode(len(periods)))
    for p in periods:
        logger.debug(u"Period is " + p)
        debates = list(Debate.objects.filter(period = p))
        logger.debug(u"Num debates in period: " + unicode(len(debates)))
        for d in debates:
            #make the list a string and drop the brackets ([])
            sts = unicode(d.spectators)[1:-1]
            string = template.substitute(period=p,
                                         location=d.location,
                                         aff_team=d.affirmative,
                                         neg_team=d.negative,
                                         spec_teams=sts)
            with open(ROLL_FILE, u'a') as f:
                f.write(string)
