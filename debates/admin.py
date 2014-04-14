#!/usr/bin/env python2.7
#file admin.py

from django.contrib.admin import autodiscover, site
from debates.models       import (
                                     Topic, Location, Date, Score, School,
                                     GoogleUser, Debater, Team, Debate,
                                     Period,
                                 )
from debates.resources    import DebaterResource, TeacherResource
from import_export.admin  import ImportExportModelAdmin
#from logging              import getLogger

#logger = getLogger('logview.debugger')

autodiscover()

class DebaterAdmin(ImportExportModelAdmin):
    resource_class = DebaterResource

class TeacherAdmin(ImportExportModelAdmin):
    resource_class = TeacherResource

site.register(Topic)
site.register(Location)
site.register(Date)
site.register(Score)
site.register(School)
site.register(GoogleUser)
site.register(Debater, DebaterAdmin)
site.register(Team)#, TeamAdmin)
site.register(Debate)
site.register(Period)
