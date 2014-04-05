import logging

logger = logging.getLogger('logview.debugger')
# Full path and name to your csv file
csv_filepathname="/AHS-Freshmen-Debates/freshmendebates/freshmen.csv"
# Full path to your django project directory
your_djangoproject_home="/AHS-Freshmen-Debates/freshmendebates/freshmendebates/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from debates.models import Student, GoogleUser

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
counter = 0
student = Student()

#logger.debug('counter is ' + counter)
for row in dataReader:
	if row[0] != 'Student Name': # Ignore the header row, import everything else
		if counter == 0:
			englishTeacher = row[2]
			englishTeacherGet = GoogleUser.objects.get(last_name = englishTeacher)
			student = Student()
			logger.debug('Student has begun')
			fullname = row[0]
			logger.debug('Students fullname ' + fullname)
			splitName = fullname.split(',' , 1)
			first_name = splitName[1]
			logger.debug('Students first name ' + first_name)
			last_name = splitName[0]
			logger.debug('Student last name ' + last_name)
			student.englishPeriod = row[1]
			logger.debug('Student has english period ' + student.englishPeriod)
			student.englishTeacher = englishTeacherGet
			logger.debug('Students english teacher is ' + englishTeacher)
			student.save()
		elif row[0] == student.first_name and count != 0:
			IHSTeacher = row[2]
			IHSTeacherGet = GoogleUser.objects.get(last_name = IHSTeacher)
			student.englishPeriod = row[1]
			logger.debug('Student has english period ' + student.englishPeriod)
			student.IHSTeacher = IHSTeacherGet
			logger.debug('Students IHS teacher is ' + IHSTeacher)
			student.save()
		elif row[3] == "900012":
			IHSTeacher = row[2]
			IHSTeacherGet = GoogleUser.objects.get(last_name = IHSTeacher)
			student = Student()
			logger.debug('Student has begun')
			fullname = row[0]
			logger.debug('Students fullname ' + fullname)
			splitName = fullname.split(',' , 1)
			first_name = splitName[1]
			logger.debug('Students first name ' + first_name)
			last_name = splitName[0]
			logger.debug('Student last name ' + last_name)
			student.first_name = first_name
			logger.debug('Student has first name '+ student.first_name)
			student.last_name = last_name
			logger.debug('Student has last name '+ student.last_name)
			student.IHSPeriod = row[1]
			logger.debug('Student has IHS period ' + student.IHSPeriod)
			student.IHSTeacher = IHSTeacherGet
			logger.debug('Students IHS teacher is ' + IHSTeacher)
		else:
			englishTeacher = row[2]
			englishTeacherGet = GoogleUser.objects.get(last_name = englishTeacher)
			logger.debug('Student has begun')
			student.first_name = first_name
			logger.debug('Student has first name '+ student.first_name)
			student.last_name = last_name
			logger.debug('Student has last name '+ student.last_name)
			student.englishPeriod = row[1]
			logger.debug('Student has english period ' + student.englishPeriod)
			student.englishTeacher = englishTeacherGet
			logger.debug('Students english teacher is ' + englishTeacher)
			student.save()
	counter += 1