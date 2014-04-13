#!/usr/bin/env python2.7
#file: load.py
#load teacher and student data

import sys
import os
sys.path.append(u'/home/djrh/Programming/AHS-Freshman-Debates/debates_site')
os.environ[u'DJANGO_SETTINGS_MODULE'] = u'settings'

from csv            import DictReader
from debates.models import Student, GoogleUser
#from logging        import getLogger

#TEACHER_DATA_FILE = 'teachers.csv'
TEACHER_FIELDS    = [u'first name', u'last name', u'email']
#DEBATER_DATA_FILE = 'debaters.csv'
DEBATER_FIELDS    = [u'first name', u'last name',
                     u'English teacher', u'English Period',
                     u'IHS teacher', u'IHS period']

#logger = getLogger('logview.debugger')

def loadTeachers(f):
    for t in parseTeachers(f):
        t.save()

def loadDebaters(f):
    for d in parseDebaters(f):
        d.save()

def parseTeachers(f):
    dicts = DictReader(f, fieldnames=TEACHER_FIELDS)
    teachers = []
    for d in dicts:
        teachers.append(dictToTeacher(d))
    return teachers

def parseDebaters(f):
    dicts = DictReader(f, fieldnames=DEBATER_FIELDS)
    debaters = []
    for d in dicts:
        debaters.append(dictToDebater(d))
    return debaters

def dictToTeacher(dictionary):
    teacher              = GoogleUser()
    teacher.first_name   = dictionary[u'first name']
    teacher.last_name    = dictionary[u'last name']
    teacher.role         = 1
    teacher.email        = dictionary[u'email']
    teacher.password     = u"p_word"
    teacher.is_admin     = False
    teacher.is_staff     = True
    teacher.is_superuser = False
    return teacher

def dictToStudent(dictionary):
    student                 = Student()
    student.first_name      = dictionary[u'first name']
    student.last_name       = dictionary[u'last name']
    student.english_teacher = GoogleUser.objects.get(last_name =
                                  dictionary[u'English teacher'])
    student.english_period  = dictionary[u'English period']
    student.ihs_teacher     = GoogleUser.objects.get(last_name =
                                  dictionary[u'IHS teacher'])
    student.ihs_period      = dictionary[u'IHS period']
