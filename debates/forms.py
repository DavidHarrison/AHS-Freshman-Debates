#!/usr/bin/env python3.4
#file: forms.py

from django.forms   import ModelForm, ChoiceField, RadioSelect, Form
from django.db      import models
from debates.models import GoogleUser, Score, Team, UploadFile

'''
SCORE_CHOICES = (
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
        )
ROLE_CHOICES = (
        ('0', 'School'),
        ('1', 'Teacher'),
        ('2', 'Judge'),
        ('3', 'Student'),
        ('4', 'Admin'),
    )
scores = ChoiceField(widget=RadioSelect(), choices=SCORE_CHOICES)
'''

class ScoreForm(ModelForm):
    class Meta:
        model = Score

class RegistrationForm(ModelForm):
    class Meta:
        model = GoogleUser

class TeamForm(ModelForm):
    class Meta:
        model = Team

class UploadFileForm(Form):
    class Meta:
        model = UploadFile
