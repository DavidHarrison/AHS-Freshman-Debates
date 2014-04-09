#!/usr/bin/env python3.4
#file: load.py
#load teacher and student data

#import sys
#import os
#sys.path.append('/home/djrh/Programming/AHS-Freshman-Debates/')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from csv            import DictReader
from debates.models import Student, GoogleUser
#from logging        import getLogger

#TEACHER_DATA_FILE = 'teachers.csv'
TEACHER_FIELDS    = ['first name', 'last name', 'email']
#DEBATER_DATA_FILE = 'debaters.csv'
DEBATER_FIELDS    = ['first name', 'last name',
                     'English teacher', 'English Period',
                     'IHS teacher', 'IHS period']

#logger = getLogger('logview.debugger')

def loadTeachers(f):
    list(map(lambda t: t.save(), parseTeachers(f)))

def loadDebaters(f):
    list(map(lambda d: d.save(), parseDebaters(f)))

def parseTeachers(f):
    dicts = DictReader(f, fieldnames=TEACHER_FIELDS)
    return list(map(dictToTeacher, dicts))

def parseDebaters(f):
    dicts = DictReader(f, fieldnames=DEBATER_FIELDS)
    return list(map(dictToDebater, dicts))

def dictToTeacher(dictionary):
    teacher              = GoogleUser()
    teacher.first_name   = dictionary['first name']
    teacher.last_name    = dictionary['last name']
    teacher.role         = 1
    teacher.email        = dictionary['email']
    teacher.password     = "p_word"
    teacher.is_admin     = False
    teacher.is_staff     = True
    teacher.is_superuser = False
    return teacher

def dictToStudent(dictionary):
    student                 = Student()
    student.first_name      = dictionary['first name']
    student.last_name       = dictionary['last name']
    student.english_teacher = GoogleUser.objects.get(last_name =
                                  dictionary['English teacher'])
    student.english_period  = dictionary['English period']
    student.ihs_teacher     = GoogleUser.objects.get(last_name =
                                  dictionary['IHS teacher'])
    student.ihs_period      = dictionary['IHS period']
