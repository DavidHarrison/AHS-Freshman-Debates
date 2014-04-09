#!/usr/bin/env python3.4
#file admin.py

from django.contrib.admin      import autodiscover, ModelAdmin, site
from django.db                 import models
from debates.models            import (
                                          Topic, Location, Date, Score, School,
                                          GoogleUser, Student, Team, Debate,
                                          Period,
                                      )

autodiscover()

#def order_by_teacher(modeladmin, request, queryset):

class TeamAdmin(ModelAdmin):
    list_filter = ['teacher']
    ordering    = ['team_number']

class StudentAdmin(ModelAdmin):
    list_display = ('last_name', 'first_name','english_teacher','ihs_teacher')
    ordering     = ['last_name']
    list_filter  = ['english_teacher','ihs_teacher','english_period']

class DateAdmin(ModelAdmin):
    ordering = ['date']
    

site.register(Topic)
site.register(Location)
site.register(Date)
site.register(Score)
site.register(School)
site.register(GoogleUser)
site.register(Student, StudentAdmin)
site.register(Team, TeamAdmin)
site.register(Debate)
site.register(Period)

try:
    from admin_import.options import add_import
except ImportError:
    pass
else:
    add_import(InviteeAdmin)
