#!/usr/bin/env python2.7
#file admin.py

from django.contrib.admin import autodiscover, site
from debates.models       import (
                                     Topic, Location, Date, Score, School,
                                     GoogleUser, Student, Team, Debate,
                                     Period,
                                 )
from debates.resources    import StudentResource, TeacherResource
from import_export.admin  import ImportExportModelAdmin
#from logging              import getLogger

#logger = getLogger('logview.debugger')

autodiscover()

class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource

class TeacherAdmin(ImportExportModelAdmin):
    resource_class = TeacherResource

site.register(Topic)
site.register(Location)
site.register(Date)
site.register(Score)
site.register(School)
site.register(GoogleUser)
site.register(Student, StudentAdmin)
site.register(Team)#, TeamAdmin)
site.register(Debate)
site.register(Period)
