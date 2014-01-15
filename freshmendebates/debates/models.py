from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.utils.timezone import utc
import pytz
from django.utils import timezone
import logging

logger = logging.getLogger('logview.debugger')
DEBATE_DAY_CHOICES = ('1st', '2nd')
PERIOD_CHOICES = ('1', '2', '3', '4', '5', '6', '7')
LOCATION_CHOICES = ('Library', 'Little_Theatre', 'Other_Location')

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

# Create models here.
class Affirmative(models.Model):	
	Speaker1 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Speaker2 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	CrossExamination = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Argument = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	SlideShowScore = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Rebuttal = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	#R = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)

class Negative(models.Model):
	Speaker1 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Speaker2 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	CrossExamination = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Argument = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	SlideShowScore = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Rebuttal = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	#R = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)

class GoogleUser(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	role = models.CharField(max_length=2, choices=ROLE_CHOICES)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=255)
	is_admin = models.BooleanField(('admin status'),default=False)
	is_staff = models.BooleanField(('staff status'),default=True)
	is_superuser = models.BooleanField(('super status'),default=False)
	date_joined = models.DateTimeField(('date joined'), default=timezone.now)
	def create_user(self, first_name, last_name, email, password):
		user = User.objects.create_user(first_name, email, password)
		user.last_name = last_name
		return user
		logger.debug('New user has been saved')	
	def __unicode__(self):
				return u'%s' % self.last_name


class Student(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	englishTeacher = models.ForeignKey(GoogleUser, related_name='EnglishTeacher')
	englishPeriod = models.CharField(max_length=255)
	IHSTeacher = models.ForeignKey(GoogleUser, related_name='IHSTeacher')
	IHSPeriod = models.CharField(max_length=255)
	def __unicode__(self):
				return u'%s' % self.last_name + ',' + self.first_name
	# class Meta:
 #    		app_label="classes"

class Team(models.Model):
 	#Start of roles -- getting students names tied into roles.
	speaker1 = models.ForeignKey(Student, related_name='student_speaker1_type')
	speaker2 = models.ForeignKey(Student, related_name='student_speaker2_type')
	crossexamination = models.ForeignKey(Student, related_name='student_cross_type')
	slideshow = models.ForeignKey(Student, related_name='student_slide_type')
	rebuttal = models.ForeignKey(Student, related_name='student_rebutt_type')
 	#End of roles
	teamnumber = models.CharField(max_length=20)
 	#Not sure about this syntax --  may want to ask terrence
	topic = models.CharField(max_length=255)
	school = models.CharField(max_length=255)
	#Is pro? True/False	
	affirmative = models.BooleanField((Affirmative), default = False)
 	#end of unknown syntax
 	teacher = models.ForeignKey(GoogleUser)
 	def __unicode__(self):
				return u'%s' % self.teamnumber


class SubmittedAffirmativeScore(models.Model):
	Speaker1 = models.CharField(max_length=3)
	Speaker2 = models.CharField(max_length=3)
	CrossExamination = models.CharField(max_length=3)
	Argument = models.CharField(max_length=3)
	SlideShowScore = models.CharField(max_length=3)
	Rebuttal = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)

	TeamNumber = models.ForeignKey(Team)
	def __unicode__(self):
				return u'%s' % self.TeamNumber

class SubmittedNegativeScore(models.Model):
	Speaker1 = models.CharField(max_length=3)
	Speaker2 = models.CharField(max_length=3)
	CrossExamination = models.CharField(max_length=3)
	Argument = models.CharField(max_length=3)
	SlideShowScore = models.CharField(max_length=3)
	Rebuttal = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)

	TeamNumber = models.ForeignKey(Team)
	def __unicode__(self):
				return u'%s' % self.TeamNumber
class Topic(models.Model):
	topic = models.CharField(max_length=25)
	description = models.CharField(max_length=255)
	def __unicode__(self):
				return u'%s' % self.topic


class Location(models.Model):
	location = models.CharField(max_length=255)
	def __unicode__(self):
				return u'%s' % self.location

	
class Date(models.Model):
	date = models.CharField(max_length=255)
	def __unicode__(self):
				return u'%s' % self.date



class School(models.Model):#Also admin
	name = models.CharField(max_length=25)
	district = models.CharField(max_length=25)
	description = models.CharField(max_length=255)
	is_staff = models.BooleanField(('staff status'),default=True)
	def __unicode__(self):
			return u'%s' % self.name

class Debate(models.Model):
 	#Affirmative team
 	affirmative = models.ForeignKey(Team, related_name='team_affirmative_type')
 	#Negative team
 	negative = models.ForeignKey(Team, related_name='team_negative_type')
 	#date of debate
 	date = models.ForeignKey(Date)
 	#Location of debate
 	location =models.ForeignKey(Location)
 	#school
 	school = models.ForeignKey(School)
 	#topic
 	topic = models.ForeignKey(Topic)



class SCORE_OPTIONS(models.Model):
	SCORE_CHOICES = [(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10')]
	scores = models.BigIntegerField(verbose_name='scores:', choices=SCORE_CHOICES)

class CustomUser(models.Manager):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(('email address'), max_length=254, unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(('staff status'), default=False,
        help_text=('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(('active'), default=True,
        help_text=('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])