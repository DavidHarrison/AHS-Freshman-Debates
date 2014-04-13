#!/usr/bin/env python2.7
#file resources.py

from import_export.resources import ModelResource
from debates.models          import Student

class StudentResource(ModelResource):
    class Meta(object):
        model = Student
