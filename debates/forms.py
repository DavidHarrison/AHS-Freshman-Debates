from django         import forms
from django.db      import models
from debates.models import GoogleUser, Score

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

class ScoreForm(forms.ModelForm):
    slideshow         = scores.choices
    speaker1          = scores.choices
    speaker2          = scores.choices
    cross_examination = scores.choices
    argument          = scores.choices
    rebuttal          = scores.choices
    team_number       = models.CharField(max_length=2)
    notes             = models.CharField(max_length=150)
    class Meta:
        model = Score

class RegistrationForm(forms.ModelForm):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    role       = models.CharField(max_length=2, choices=ROLE_CHOICES)
    email      = models.CharField(max_length=30)
    password   = models.CharField(max_length=255)
    class Meta:
        model = GoogleUser

class ImportExcelForm(forms.Form):
    file = forms.FileField()
    def save(self):
        records = csv.reader(self.cleaned_data('file'), delimiter=',',
                             quotechar='"')
        for row in record:
            # Ignore the header row, import everything else
            if row[0] != 'Student Name':
                if row[0] != input_student.fullname:
                    english_teacher = GoogleUser.objects.get(last_name = row[2])
                    #TODO, find function
                    input_student = student()
                    split_name = row[0].split(',' , 1)
                    input_student.first_name = split_name[1]
                    input_student.last_name  = split_name[0]
                    input_data.save()
                        
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()
        
        
#class Team(forms.ModelForm):
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
