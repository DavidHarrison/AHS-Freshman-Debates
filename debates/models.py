#!/usr/bin/env python2.7
#file: models.py

from django.db.models import (
                                 BooleanField, CharField, DateTimeField,
                                 TextField, ForeignKey, IntegerField,
                                 ManyToManyField, EmailField, FileField,
                                 Model, Manager
                             )
from django.utils     import timezone
from logging          import getLogger

logger = getLogger(u'logview.debugger')

#DEBATE_DAY_CHOICES = ('1st', '2nd')
#PERIOD_CHOICES     = ('1', '2', '3', '4', '5', '6', '7')
#LOCATION_CHOICES   = ('Library', 'Little Theatre', 'Other Location')
SCORE_CHOICES = (
        ('5',  '5'),
        ('6',  '6'),
        ('7',  '7'),
        ('8',  '8'),
        ('9',  '9'),
        ('10', '10'),
    )
ROLE_CHOICES = (
        ('0', 'School'),
        ('1', 'Teacher'),
        ('2', 'Judge'),
        ('3', 'Student'),
        ('4', 'Admin'),
    )

#Also admin
class School(Model):
    name        = CharField(max_length=25)
    district    = CharField(max_length=25)
    description = CharField(max_length=150)
    #TODO, what does this do?
    #is_staff    = BooleanField(('staff status'),default=True)

    def __unicode__(self):
        return '%s' % self.name
            
class Topic(Model):
    name        = CharField(max_length=25)
    description = CharField(max_length=150)

    def __unicode__(self):
        return '%s' % self.topic

class GoogleUser(Model):
    first_name  = CharField(max_length=50)
    last_name   = CharField(max_length=50)
    role        = CharField(max_length=2, choices=ROLE_CHOICES)
    email       = CharField(max_length=30)
    password    = CharField(max_length=150)
    date_joined = DateTimeField("date joined", default=timezone.now)

    def __unicode__(self):
        return '%s' % self.last_name

#TODO, should probably be changed to Debater (Judges are also students)
class Student(Model):
    first_name      = CharField(max_length=255)
    last_name       = CharField(max_length=255)
    #english_teacher = ForeignKey(GoogleUser,
    #                             related_name=u'EnglishTeacher')
    english_teacher = CharField(max_length=255)
    english_period  = CharField(max_length=255)
    #ihs_teacher     = ForeignKey(GoogleUser,
    #                             related_name=u'IHSTeacher')
    ihs_teacher     = CharField(max_length=255)
    ihs_period      = CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.last_name + ', ' + self.first_name
    
    class Meta:
        #TODO, can it be assured that no two student will have the same
        #first/last name combination (unlikely but possible)?
        unique_together = ('first_name', 'last_name')

class Team(Model):
    #TODO, are these redundant to the roles? If not, could they be done as
    #a list?
    '''
    student1            = ForeignKey(Student,
                                  related_name='student1_type')
    student2            = ForeignKey(Student,
                                  related_name='student2_type')
    student3            = ForeignKey(Student,
                                  related_name='student3_type')
    student4            = ForeignKey(Student,
                                  related_name='student4_type')
    student5            = ForeignKey(Student,
                                  related_name='student5_type',
                                  blank = True)
    '''
    #Start of roles -- getting students names tied into roles.
    '''
    speaker1            = ForeignKey(Student,
                                  related_name='student_speaker1_type',
                                  blank=True)
    speaker2            = ForeignKey(Student,
                                  related_name='student_speaker2_type',
                                  blank=True)
    cross_examiner      = ForeignKey(Student,
                                  related_name='student_cross_type',
                                  blank=True)
    slideshow_presenter = ForeignKey(Student,
                                  related_name='student_slide_type',
                                  blank=True)
    rebutter            = ForeignKey(Student,
                                  related_name='student_rebutt_type',
                                  blank=True)
    '''
    speaker1            = CharField(max_length=50)
    speaker2            = CharField(max_length=50)
    cross_examiner      = CharField(max_length=50)
    slideshow_presenter = CharField(max_length=50)
    rebutter            = CharField(max_length=50)
    #End of roles
    team_number         = CharField(max_length=20)
    team_name           = CharField(max_length=50)
    topic               = ForeignKey(Topic)
    school              = ForeignKey(School)
    #Is aff? True/False    
    is_aff              = BooleanField(default = False)
    teacher             = ForeignKey(GoogleUser)

    def __unicode__(self):
        return '%s' % self.team_number

class Score(Model):
    speaker1          = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    speaker2          = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    cross_examination = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    argument          = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    slideshow         = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    rebuttal          = CharField(max_length=2, choices=SCORE_CHOICES,
                                 default=5)
    team_number       = CharField(max_length=2)
    notes             = CharField(max_length=150)
    is_aff            = BooleanField(default = False)

    def __unicode__(self):
        return '%s' % self.team_number

class Location(Model):
    location = CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.location

class Period(Model):
    period = IntegerField(max_length=2)

    def __unicode__(self):
        return '%s' % self.period
    
class Date(Model):
    date = DateTimeField()

    def __unicode__(self):
        return '%s' % self.date

class Debate(Model):
    #Affirmative team
    affirmative = ForeignKey(Team, related_name=u'team_affirmative_type')
    #Negative team
    negative    = ForeignKey(Team, related_name=u'team_negative_type')
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
        return '%s' % self.topic
