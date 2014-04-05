from   django.db.models            import (
                                              BooleanField, CharField,
                                              DateTimeField, TextField,
                                              ForeignKey, IntegerField,
                                              ManyToManyField, EmailField,
                                              Model, Manager
                                          )
from   django.contrib.auth.models  import Group
from   django.contrib.auth.models  import User
from   django.contrib              import admin
from   django.core.urlresolvers    import reverse
from   django.forms.extras.widgets import SelectDateWidget
import datetime
from   django.utils.timezone       import utc
import pytz
from   django.utils                import timezone
import logging
#probably more work than its worth, see load.py in freshman debates for parser
#from   csvImporter.model           import CsvDbModel
from   django.forms                import CheckboxSelectMultiple
from   django.forms.models         import ModelMultipleChoiceField
from   django                      import forms
from   django.forms.widgets        import RadioSelect, CheckboxSelectMultiple

logger             = logging.getLogger('logview.debugger')
DEBATE_DAY_CHOICES = ('1st', '2nd')
PERIOD_CHOICES     = ('1', '2', '3', '4', '5', '6', '7')
LOCATION_CHOICES   = ('Library', 'Little Theatre', 'Other Location')

SCORE_CHOICES = (
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
ROLE_CHOICES = (
        ('0', 'School'),
        ('1', 'Teacher'),
        ('2', 'Judge'),
        ('3', 'Student'),
        ('4', 'Admin'),
    )

class School(Model):#Also admin
    name        = CharField(max_length=25)
    district    = CharField(max_length=25)
    description = CharField(max_length=150)
    is_staff    = BooleanField(('staff status'),default=True)

    def __unicode__(self):
        return u'%s' % self.name
            
class Topic(Model):
    topic       = CharField(max_length=25)
    description = CharField(max_length=150)

    def __unicode__(self):
        return u'%s' % self.topic

class GoogleUser(Model):
    first_name  = CharField(max_length=50)
    last_name   = CharField(max_length=50)
    role        = CharField(max_length=2, choices=ROLE_CHOICES)
    email       = CharField(max_length=30)
    password    = CharField(max_length=150)
    date_joined = DateTimeField("date joined", default=timezone.now)

    """
    def create_user(self, first_name, last_name, email, password, role):
        user = User.objects.create_user(username = first_name, email = email,
                                        password = password)
        user.first_name = first_name
        user.last_name = last_name
        if role == 0 or role == 1:
            user.is_staff = True
        #TODO, figure what this is for
        if role == 1:
            g = Group.objects.get(name='Teachers') 
        g.user_set.add(user)
        logger.debug('teacher password ' + password)
        user.save()
        return user
        logger.debug('New user has been saved')    
    """

    def __unicode__(self):
        return u'%s' % self.last_name

class Student(Model):
    first_name     = CharField(max_length=255)
    last_name      = CharField(max_length=255)
    english_teacher = ForeignKey(GoogleUser,
                                       related_name='EnglishTeacher')
    english_period  = CharField(max_length=255)
    ihs_teacher     = ForeignKey(GoogleUser,
                                       related_name='IHSTeacher')
    ihs_period      = CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.last_name + ', ' + self.first_name

    #class Meta:
        #app_label="classes"

# class MyCsvModel(CsvDbModel):
#     class Meta:
#         dbModel = Student
#         delimiter = ","

class Team(Model):
    Student_1        = ForeignKey(Student,
                                  related_name='student1_type')
    Student_2        = ForeignKey(Student,
                                  related_name='student2_type')
    Student_3        = ForeignKey(Student,
                                  related_name='student3_type')
    Student_4        = ForeignKey(Student,
                                  related_name='student4_type')
    Student_5        = ForeignKey(Student,
                                  related_name='student5_type',
                                  blank = True)
    #Start of roles -- getting students names tied into roles.
    speaker_1        = ForeignKey(Student,
                                  related_name='student_speaker1_type',
                                  blank=True)
    speaker_2        = ForeignKey(Student,
                                  related_name='student_speaker2_type',
                                  blank=True)
    crossexamination = ForeignKey(Student,
                                  related_name='student_cross_type',
                                  blank=True)
    slideshow        = ForeignKey(Student,
                                  related_name='student_slide_type',
                                  blank=True)
    rebuttal         = ForeignKey(Student,
                                  related_name='student_rebutt_type',
                                  blank=True)
    #End of roles
    team_Number      = CharField(max_length=20)
    #Not sure about this syntax --  may want to ask Terence
    topic            = ForeignKey(Topic)
    school           = ForeignKey(School)
    #Is aff? True/False    
    affirmative      = BooleanField(default = False)
    #end of unknown syntax
    teacher          = ForeignKey(GoogleUser)

    def __unicode__(self):
        return u'%s' % self.team_Number

class Form(Model):
    Speaker1         = CharField(max_length=2, choices=SCORE_CHOICES,
                                        blank = False)
    Speaker2         = CharField(max_length=2, choices=SCORE_CHOICES,
                                        blank = False)
    Speaker3         = CharField(max_length=2, choices=SCORE_CHOICES,
                                        blank = True)
    CrossExamination = CharField(max_length=2, choices=SCORE_CHOICES,
                                        blank = False)
    SlideShowScore   = CharField(max_length=2, choices=SCORE_CHOICES,
                                        blank = False)
    Rebuttal         = CharField(max_length=2, choices=SCORE_CHOICES,
                                        blank = False)
    Argument         = CharField(max_length=2, choices=SCORE_CHOICES,
                                        blank = False)
    #R = CharField(max_length=2, choices=SCORE_CHOICES, default=5)
    TeamNumber       = ForeignKey(Team)
    Notes            = TextField(max_length = 150)

class SubmittedOverallScore(Model):
    Speaker1         = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    Speaker2         = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    CrossExamination = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    Argument         = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    SlideShowScore   = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    Rebuttal         = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    TeamNumber       = ForeignKey(Team)
    isAff            = BooleanField(default = False)

    def __unicode__(self):
        return u'%s' % self.TeamNumber

class Location(Model):
    location = CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.location

class Period(Model):
    period = IntegerField(max_length=2)

    def __unicode__(self):
        return u'%s' % self.period
    
class Date(Model):
    date = DateTimeField()

    def __unicode__(self):
        return u'%s' % self.date

class Debate(Model):
    #Affirmative team
    affirmative = ForeignKey(Team, related_name='team_affirmative_type')
    #Negative team
    negative    = ForeignKey(Team, related_name='team_negative_type')
    #date of debate
    date        = ForeignKey(Date)
    #Location of debate
    location    = ForeignKey(Location)
    #Period
    period      = ForeignKey(Period)
    #school
    school      = ForeignKey(School)
    #topic
    topic       = ForeignKey(Topic)
    #spectators
    spectators  = ManyToManyField(Team, blank=True)

    def __unicode__(self):
        return u'%s' % self.topic

class CustomUser(Manager):
    # A fully featured User model with admin-compliant permissions that uses
    # a full-length email field as the username.
    # Email and password are required. Other fields are optional.
    email       = EmailField(('email address'), max_length=254,
                                    unique=True)
    first_name  = CharField(('first name'), max_length=30, blank=True)
    last_name   = CharField(('last name'), max_length=30, blank=True)
    is_staff    = BooleanField(('staff status'), default=False,
        help_text=('Designates whether the user can log into this admin '
                    'site.'))
    is_active  = BooleanField(('active'), default=True,
        help_text=('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = DateTimeField(('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        # Returns the first_name plus the last_name, with a space in between.
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        # Returns the short name for the user.
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        # Sends an email to this User.
        send_mail(subject, message, from_email, [self.email])
