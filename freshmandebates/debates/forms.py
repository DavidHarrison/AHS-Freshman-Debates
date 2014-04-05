from django import forms
from django.db import models
from debates.models import GoogleUser
from django.forms import ModelForm
from debates.models import Affirmative_form,Negative_form
from django.forms import CheckboxSelectMultiple

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
scores = forms.ChoiceField(widget=forms.RadioSelect(), choices=SCORE_CHOICES)


class AffirmativeScore(ModelForm):
		SlideShowScore = scores.choices
		Speaker1 = scores.choices
		Speaker2 = scores.choices
		CrossExamination = scores.choices
		Argument = scores.choices
		Rebuttal = scores.choices
		class Meta:
			model = Affirmative_form
class NegativeScore(ModelForm):
		SlideShowScore = scores.choices
		Speaker1 = scores.choices
		Speaker2 = scores.choices
		CrossExamination = scores.choices
		Argument = scores.choices
		Rebuttal = scores.choices
		class Meta:
			model = Negative_form
class RegistrationForm(ModelForm):
		FirstName = models.CharField(max_length=255)
		LastName = models.CharField(max_length=255)
		role = models.CharField(max_length=2, choices=ROLE_CHOICES)
		email = models.CharField(max_length=30)
		password = models.CharField(max_length=255)
		class Meta:
			model = GoogleUser

class ImportExcelForm(forms.Form):
    	file  = forms.FileField(label= "Choose excel to upload")

# class Team(ModelForm):
# 		DebateTopic = 
# 		Side = 
# 		TeamNumber = 
# 		TeamName = 
# 		SlideShowSpeaker = 
# 		Speaker1 = 
# 		Speaker2 = 
# 		CrossExamination = 
# 		Rebuttal = 
# 		class Meta:
# 			model = Team