#!/usr/bin/env python2.7
#file: manage.py

import os
import sys

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'debates_site.settings'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
