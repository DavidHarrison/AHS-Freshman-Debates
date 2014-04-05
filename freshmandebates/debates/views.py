from django.shortcuts import render, get_object_or_404
from debates.models import Topic,Location,Date,User,Affirmative_form,Negative_form,SubmittedAffirmativeScore,SubmittedNegativeScore,GoogleUser,Student
from debates.forms import AffirmativeScore,NegativeScore,RegistrationForm,ImportExcelForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.utils.timezone import utc
import logging

logger = logging.getLogger('logview.debugger')


# Create your views here.


#get the debate that are on
def judge(request):
	Submit_form = 'null'
	Affform = AffirmativeScore()
	Negform = NegativeScore()
	if request.method == 'GET':
		Affform = AffirmativeScore()
		Negform = NegativeScore()
		logger.debug('Getting request method GET!')
	elif request.method == 'POST':
		logger.debug('Getting request method Post!')
		logger.debug(request.POST)
	 	if 'form_Positive' in request.POST:
	 		logger.debug('Form is Positive')
			Affform = AffirmativeScore(request.POST)
			Submit_form = 'aff'
	 		if Affform.is_valid():
	 			#temp storage of Data from form
				S1 = Affform.cleaned_data.get('Speaker1')
				S2 = Affform.cleaned_data.get('Speaker2')
				CE = Affform.cleaned_data.get('CrossExamination')
				SSS = Affform.cleaned_data.get('SlideShowScore')
				Arg = Affform.cleaned_data.get('Argument')
				RB = Affform.cleaned_data.get('Rebuttal')
				TN = Affform.cleaned_data.get('Team')
				#creating an instance of submitted scores to save to data base.
				p = SubmittedAffirmativeScore()
				p.Speaker1 = S1
				p.Speaker2 = S2
				p.CrossExamination = CE
				p.SlideShowScore = SSS
				p.Argument = Arg
				p.Rebuttal = RB
				p.TeamNumber = ''
				p.save()
				logger.debug('Negative form has been saved')
		elif 'form_Negative' in request.POST:
			logger.debug('Form is Negative')
			Negform = NegativeScore(request.POST)
			Submit_form = 'neg'
			if Negform.is_valid():
				#temp storage of Data from form
				S1 = Negform.cleaned_data.get('Speaker1')
				S2 = Negform.cleaned_data.get('Speaker2')
				CE = Negform.cleaned_data.get('CrossExamination')
				SSS = Negform.cleaned_data.get('SlideShowScore')
				Arg = Negform.cleaned_data.get('Argument')
				RB = Negform.cleaned_data.get('Rebuttal')
				TN = Negform.cleaned_data.get('Team')
				logger.debug('Negative form is valid!')
				#creating an instance of submitted scores to save to data base.
				p = SubmittedNegativeScore()
				p.Speaker1 = S1
				p.Speaker2 = S2
				p.CrossExamination = CE
				p.SlideShowScore = SSS
				p.Argument = Arg
				p.Rebuttal = RB
				p.TeamNumber = ''
				p.save()
				logger.debug('Negative form has been saved')
				#msg = "The operation has been received correctly."
				#print request.POST
				#return render_to_response('debates/scoring_upload.html', {'msg':msg}, context_instance=RequestContext(request))
				#return render_to_response(msg)
		if request.is_ajax():
			logger.debug('Request is ajax')
			msg = "The operation has been received correctly."
			logger.debug(msg)

	return render(request,'debates/judge.html', {
		'Affirmative_Form':Affform, 'Negative_Form':Negform,
	})
def new_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            logger.debug(first_name)
            last_name = form.cleaned_data.get('last_name')
            logger.debug(last_name)
            role = form.cleaned_data.get('role')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            new_registered_user = GoogleUser()
            new_registered_user.first_name = first_name
            new_registered_user.last_name = last_name
            new_registered_user.email = email
            new_registered_user.role = role
            new_registered_user.password = password
            new_registered_user.is_admin = False
            new_registered_user.is_staff = True
            new_registered_user.is_superuser = False
            new_registered_user.save()
            new_registered_user.create_user(first_name,last_name,email,password)
    else:
        form = RegistrationForm()

	return render(request,'debates/new_user.html',  {
		'Form':form,
	})

def handle(request):

	Affirmative_Scores = Affirmative.objects.all()
	Negative_Scores = Negative.objects.all()

	return render(request,'debates/scoring_upload.html', {
		'Affirmative_Scores':Affirmative_Scores, 'Negative_Scores':Negative_Scores,
	})

def splash(request):

	return render(request,'debates/Splash.html', {
	})

def teacher(request):
 	
 	Index = SubmittedAffirmativeScore.objects.filter(TeamNumber = 'Test, still need to get team numbers')
 	Team = get_object_or_404(SubmittedAffirmativeScore)

	return render(request,'debates/Teacher.html', {
		'Team': Team
	})

def teacherselector(request):

	return render(request,'debates/TeacherSelector.html', {
	}) 

def teamcreate(request):

	return render(request,'debates/TeamCreate.html', {
	})	

def debateselector(request):

	return render(request,'debates/DebateSelector.html', {
	})

def test_flowcell(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ImportExcelForm(request.POST,  request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            excel_parser= ExcelParser()
            success, log  = excel_parser.read_excel(request.FILES['file'] )
            if success:
                return redirect(reverse('admin:index') + "pages/flowcell_good/") ## redirects to aliquot page ordered by the most recent
            else:
                errors = '* Problem with flowcell * <br><br>log details below:<br>' + "<br>".join(log)
    else:
        form = ImportExcelForm() # An unbound form
    return render(request,'debates/file_upload.html',{
    	'form':form,
    	})

def databasesetup(request):
	
	#my_csv_list = MyCsvModel.import_data(data = open("/AHS-Freshmen-Debates/freshmendebates/freshmen.csv"))
	#first_line = my_csv_list[0]  

	return render(request,'debates/judge.html',{
	})


