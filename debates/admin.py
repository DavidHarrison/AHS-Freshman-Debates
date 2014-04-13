#!/usr/bin/env python2.7
#file admin.py

from django.contrib.admin import autodiscover, ModelAdmin, site
from django.db            import models
from debates.models       import (
                                     Topic, Location, Date, Score, School,
                                     GoogleUser, Student, Team, Debate,
                                     Period,
                                 )
from debates.resources    import StudentResource
from django.conf.urls     import patterns
#from debates.views        import import_debaters
from import_export.admin  import ImportExportModelAdmin

autodiscover()

#def order_by_teacher(modeladmin, request, queryset):

'''
class TeamAdmin(ModelAdmin):
    list_filter = ['teacher']
    ordering    = ['team_number']

class StudentAdmin(ModelAdmin):
    list_display = ('last_name', 'first_name','english_teacher','ihs_teacher')
    #ordering     = ['last_name']
    #list_filter  = ['english_teacher','ihs_teacher','english_period']

    def get_urls(self):
        urls = super(StudentAdmin, self).get_urls()
        my_urls = patterns('',
                      (r'^import/$', self.admin_site.admin_view(import_debaters))
                  )
        return my_urls + urls

class DateAdmin(ModelAdmin):
    ordering = ['date']
'''

class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    pass
    

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

'''
try:
    from admin_import.options import add_import
except ImportError:
    pass
else:
    add_import(StudentAdmin, add_button=True)
'''
