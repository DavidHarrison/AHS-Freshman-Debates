import logging
logger = logging.getLogger('logview.debugger')

your_djangoproject_home="/AHS-Freshmen-Debates/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'freshmendebates.settings'

from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.db import models
from debates.models import GoogleUser

from django.utils import timezone
# Full path to your django project directory
your_djangoproject_home="/AHS-Freshmen-Debates/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from debates.models import Student, GoogleUser

teacher = GoogleUser()

teacher.first_name = 'Emily'
teacher.last_name = 'Surowitz'
teacher.role = 1
teacher.email = 'esurowitz@ausdk12.org'
teacher.password = 'p_word'
teacher.is_admin = False
teacher.is_staff = True
teacher.is_superuser = False

teacher.save()
teacher.create_user(teacher.first_name, teacher.last_name, teacher.email, teacher.password, teacher.role)

teacher = GoogleUser()

teacher.first_name = 'Avram'
teacher.last_name = 'Wild'
teacher.role = 1
teacher.email = 'awild@ausdk12.org'
teacher.password = 'p_word'
logger.debug('Teachers password is ' + teacher.password)
teacher.is_admin = False
teacher.is_staff = True
teacher.is_superuser = False

teacher.save()
teacher.create_user(teacher.first_name, teacher.last_name, teacher.email, teacher.password, teacher.role)

teacher = GoogleUser()

teacher.first_name = 'Corinne'
teacher.last_name = 'Dolci'
teacher.role = 1
teacher.email = 'cberletti@ausdk12.org'
teacher.password = 'p_word'
teacher.is_admin = False
teacher.is_staff = True
teacher.is_superuser = False

teacher.save()
teacher.create_user(teacher.first_name, teacher.last_name, teacher.email, teacher.password, teacher.role)

teacher = GoogleUser()

teacher.first_name = 'Jessica'
teacher.last_name = 'Park'
teacher.role = 1
teacher.email = 'jpark@ausdk12.org'
teacher.password = 'p_word'
teacher.is_admin = False
teacher.is_staff = True
teacher.is_superuser = False

teacher.save()
teacher.create_user(teacher.first_name, teacher.last_name, teacher.email, teacher.password, teacher.role)

teacher = GoogleUser()

teacher.first_name = 'Robert'
teacher.last_name = 'Lent'
teacher.role = 1
teacher.email = 'rlent@ausdk12.org'
teacher.password = 'p_word'
teacher.is_admin = False
teacher.is_staff = True
teacher.is_superuser = False

teacher.save()
teacher.create_user(teacher.first_name, teacher.last_name, teacher.email, teacher.password, teacher.role)

teacher = GoogleUser()

teacher.first_name = 'Sandy'
teacher.last_name = 'Hsiao-Frates'
teacher.role = 1
teacher.email = 'shsiao-frates@ausdk12.org'
teacher.password = 'p_word'
teacher.is_admin = False
teacher.is_staff = True
teacher.is_superuser = False

teacher.save()
teacher.create_user(teacher.first_name, teacher.last_name, teacher.email, teacher.password, teacher.role)

teacher = GoogleUser()

teacher.first_name = 'Mariflorence'
teacher.last_name = 'Hudson'
teacher.role = 1
teacher.email = 'mhudson@ausdk12.org'
teacher.password = 'p_word'
teacher.is_admin = False
teacher.is_staff = True
teacher.is_superuser = False

teacher.save()
teacher.create_user(teacher.first_name, teacher.last_name, teacher.email, teacher.password, teacher.role)

teacher = GoogleUser()

teacher.first_name = 'Unknown'
teacher.last_name = 'Huynh'
teacher.role = 1
teacher.email = 'uhuynh@ausdk12.org'
teacher.password = 'p_word'
teacher.is_admin = False
teacher.is_staff = True
teacher.is_superuser = False

teacher.save()
teacher.create_user(teacher.first_name, teacher.last_name, teacher.email, teacher.password, teacher.role)

