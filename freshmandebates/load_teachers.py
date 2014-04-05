import logging
import sys
import os
from   django.forms.extras.widgets import SelectDateWidget
import datetime
from   django.db                   import models
from   debates.models              import GoogleUser
from   django.utils                import timezone
from   debates.models              import Student, GoogleUser
from   csvImporter

logger = logging.getLogger('logview.debugger')
your_djangoproject_home = "/AHS-Freshman-Debates/"
sys.path.append(your_djangoproject_home)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'freshmendebates.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# TODO, load csv of teachers as dictionary
f = open('teachers.csv')
teacher_dicts = load(f)

for teacher_dict in teacher_dicts:
    teacher = fillTeacher(teacher_dict, GoogleUser())
    teacher.save()
    teacher.create_user(teacher.first_name, teacher.last_name, teacher.email,
                        teacher.password, teacher.role)

def fillTeacher(teacher_dict, teacher):
    teacher.first_name   = teacher_dict['first_name']
    teacher.last_name    = teacher_dict['last_name']
    teacher.role         = 1
    teacher.email        = teacher_dict['email']
    teacher.password     = 'p_word'
    teacher.is_admin     = False
    teacher.is_staff     = True
    teacher.is_superuser = False
    return teacher
