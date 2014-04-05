from django         import forms
from django.db      import models
from debates.models import GoogleUser
from django.forms   import ModelForm
from debates.models import Form
from django.forms   import CheckboxSelectMultiple

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


class OverallScore(ModelForm):
    SlideShowScore   = scores.choices
    Speaker1         = scores.choices
    Speaker2         = scores.choices
    CrossExamination = scores.choices
    Argument         = scores.choices
    Rebuttal         = scores.choices
    #isAff           = ?
    class Meta:
        model = Form

class RegistrationForm(ModelForm):
    FirstName = models.CharField(max_length=255)
    LastName  = models.CharField(max_length=255)
    role      = models.CharField(max_length=2, choices=ROLE_CHOICES)
    email     = models.CharField(max_length=30)
    password  = models.CharField(max_length=255)
    class Meta:
        model = GoogleUser

class ImportExcelForm(forms.Form):
    file = forms.FileField()
    def save(self):
        records = csv.reader(self.cleaned_data('file'), delimiter=',', quotechar='"')
        for line in record:
            if row[0] != 'Student Name': # Ignore the header row, import everything else
                if row[0] != input_student.fullname:
                    englishTeacher = row[2]
                    englishTeacherGet = GoogleUser.objects.get(last_name = englishTeacher)
                    input_student = student()
                    fullname  = row[0]
                    splitName = fullname.split(',' , 1)
                    input_student.first_name = splitName[1]
                    input_student.last_name  = splitName[0]
                    input_data.save()
                        
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()
        
        
#class Team(ModelForm):
#    DebateTopic      = 
#    Side             = 
#    TeamNumber       = 
#    TeamName         = 
#    SlideShowSpeaker = 
#    Speaker1         = 
#    Speaker2         = 
#    CrossExamination = 
#    Rebuttal         = 
#    class Meta:
#        model = Team
