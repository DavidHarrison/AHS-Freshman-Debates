from django.contrib.admin      import autodiscover, ModelAdmin, site
from django.db                 import models
from debates.models            import (
                                          Topic, Location, Date,
                                          SubmittedOverallScore, School,
                                          GoogleUser, Student, Team,
                                          Debate, Period,
                                          #StudentAdmin, TeamAdmin
                                      )
from debates.forms             import (
                                          OverallScore, RegistrationForm,
                                          ImportExcelForm, UploadFileForm
                                      )

autodiscover()

#def order_by_teacher(modeladmin, request, queryset):

class TeamAdmin(ModelAdmin):
    list_filter = ['teacher']
    ordering    = ['team_Number']

class StudentAdmin(ModelAdmin):
    list_display = ('last_name', 'first_name','englishTeacher','IHSTeacher')
    ordering     = ['last_name']
    list_filter  = ['englishTeacher','IHSTeacher','englishPeriod']

class DateAdmin(ModelAdmin):
    ordering = ['date']
    

site.register(Topic)
site.register(Location)
site.register(Date)
site.register(SubmittedOverallScore)
site.register(School)
site.register(GoogleUser)
site.register(Student)#, StudentAdmin)
site.register(Team)#, TeamAdmin)
site.register(Debate)
site.register(Period)

try:
    from admin_import.options import add_import
except ImportError:
    pass
else:
    add_import(InviteeAdmin)
