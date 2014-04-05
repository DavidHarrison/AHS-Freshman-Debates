import logging

logger = logging.getLogger('logview.debugger')
# Full path and name to your csv file
csv_filepathname="/AHS-Freshmen-Debates/freshmendebates/freshmen.csv"
# Full path to your django project directory
your_djangoproject_home="/AHS-Freshmen-Debates/freshmendebates/freshmendebates/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from debates.models import Student, GoogleUser, SubmittedAffirmativeScore, SubmittedNegativeScore, Team
totalAffirmative = SubmittedAffirmativeScore.objects.count()
totalNegative = SubmittedNegativeScore.objects.count()

Affirmative_list = list(SubmittedAffirmativeScore.objects.all())
Negative_list = list(SubmittedNegativeScore.objects.all())
Team_list = list(Team.objects.all())
counter = 0

totalNumberOfTeams = Team.objects.count()

logger.debug('Getting to for loop')
logger.debug('number of teams: ')
logger.debug(totalNumberOfTeams)
for counter in xrange(0,totalNumberOfTeams):
	logger.debug('Getting in for loop for the ')
	logger.debug(counter)
	logger.debug('time')
	team = Team_list[counter]
	teamNumber = team.teamnumber
	teamSide = team.affirmative
	logger.debug('Team number is ' + teamNumber)
	if teamSide:
		logger.debug('Team grab ' + teamNumber)
		score_list = SubmittedAffirmativeScore.objects.all().filter(TeamNumber = teamNumber)
		logger.debug('debug')
		count = 0
		for count in xrange(0,score_list.count()):
			Score_total_Rebuttal = 0
			Score_total_Speaker1 = 0
			Score_total_Speaker2 = 0
			Score_total_SlideShow = 0
			Score_total_CrossExamination = 0
			Score_total_Argument = 0

			scores = score_list[count]
			Score_total_Speaker1 += scores.Speaker1
			Score_total_Speaker2 += scores.Speaker1
			Score_total_SlideShow += scores.SlideShowScore
			Score_total_Rebuttal += scores.Rebuttal
			Score_total_Argument += scores.Argument

		Score_Sepaker1_Final = Score_total_Speaker1/score_list.count()
		Score_Sepaker2_Final = Score_total_Speaker2/score_list.count()
		Score_Slideshow_Final = Score_total_SlideshowScore/score_list.count()
		Score_Rebuttal_Final = Score_total_Rebuttal/score_list.count()
		Score_Argument_Final = Score_total_Argument/score_list.count()
	else:
		score_list = list(SubmittedNegativeScore.objects.filter(teamnumber = teamNumber))
		count = 0
		for count in xrange(0,score_list.count()):
			Score_total_Rebuttal = 0
			Score_total_Speaker1 = 0
			Score_total_Speaker2 = 0
			Score_total_SlideShow = 0
			Score_total_CrossExamination = 0
			Score_total_Argument = 0

			scores = score_list[count]
			Score_total_Speaker1 += scores.Speaker1
			Score_total_Speaker2 += scores.Speaker1
			Score_total_SlideShow += scores.SlideShowScore
			Score_total_Rebuttal += scores.Rebuttal
			Score_total_Argument += scores.Argument

		Score_Sepaker1_Final = Score_total_Speaker1/score_list.count()
		Score_Sepaker2_Final = Score_total_Speaker2/score_list.count()
		Score_Slideshow_Final = Score_total_SlideshowScore/score_list.count()
		Score_Rebuttal_Final = Score_total_Rebuttal/score_list.count()
		Score_Argument_Final = Score_total_Argument/score_list.count()

	f = open("Scores.txt", "w")
	logger.debug('File has been created with the name ' + f.name)
	f.write('Team ' + teamNumber + ' got an overall argument score of ' + Score_Argument_Final + '.')
	f.write(' The Speaker 1 score was: ' + Score_Sepaker1_Final + '.')
	f.write(' The Speaker 2 score was: ' + Score_Sepaker2_Final + '.')
	f.write(' The Slide Show score was: ' + Score_SlideShow_Final + '.')
	f.write(' The Rebuttal score was: ' + Score_Rebuttal_Final + '.')
	f.write(' The Argument score was: ' + Score_Argument_Final + '.')
	f.close
	counter += 1



