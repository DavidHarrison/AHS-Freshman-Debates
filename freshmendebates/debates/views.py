from django.shortcuts import render, get_object_or_404
from debates.models import Topic,Location,Date,Teacher
from debates.forms import AffirmativeScore,NegativeScore
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Create your views here.


#get the debate that are on
def judge(request):	
	Submit_form = 'null'
	Affform = AffirmativeScore()
	Negform = NegativeScore()
	if request.method == 'GET':
		Affform = AffirmativeScore()
		Negform = NegativeScore()
	elif request.method == 'POST' and request.is_ajax:
	 	if 'form_Positive' in request.POST:
			Affform = AffirmativeScore(request.POST)
			Submit_form = 'aff'
	 		if Affform.is_valid():
				Speaker1 = Affform.cleaned_data.get('Speaker1')
				Speaker2 = Affform.cleaned_data.get('Speaker2')
				CrossExamination = Affform.cleaned_data.get('CrossExamination')
				SlideShowScore = Affform.cleaned_data.get('SlideShowScore')
				Argument = Affform.cleaned_data.get('Argument')
				msg = "The operation has been received correctly."
				print request.POST
				#return render_to_response(msg)
		elif 'form_Negative' in request.POST:
			Negform = NegativeScore(request.POST)
			Submit_form = 'neg'
			if Negform.is_valid():
				SlideShowScore = Negform.cleaned_data.get('SlideShowScore')
				Speaker1 = Negform.cleaned_data.get('Speaker1')
				Speaker2 = Negform.cleaned_data.get('Speaker2')
				CrossExamination = Negform.cleaned_data.get('CrossExamination')
				Argument = Negform.cleaned_data.get('Argument')
				msg = "The operation has been received correctly."
				print request.POST
				#return render_to_response(msg)
#Now return the rendered template
	return render(request,'debates/judge.html', {
		'form1':Affform, 'form2':Negform,
	})

def handle(request):

	return render(request,'debates/scoring_upload.html', {
	})