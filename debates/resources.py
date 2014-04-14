#!/usr/bin/env python2.7
#file resources.py

from import_export.resources import ModelResource
from import_export.fields    import Field
from debates.models          import Debater, GoogleUser
from debates.merge_debaters  import mergeDebaters
from logging                 import getLogger

logger = getLogger('logview.debugger')

class DebaterResource(ModelResource):
    #CSV Fields
    name      = Field(column_name='Student Name')
    period    = Field(column_name='Period',       readonly=True)
    teacher   = Field(column_name='Teacher.',     readonly=True)
    course_id = Field(column_name='Course.',      readonly=True)
    
    def before_import(self, dataset, dry_run):
        #assignment of .dict needed to carry data over into calling function
        dataset.dict = mergeDebaters(dataset).dict

    class Meta(object):
        model = Debater
        #fields = ('first_name','last_name',
        #          'english_period','english_teacher',
        #          'ihs_period','ihs_teacher')
        exclude = ('name', 'period', 'teacher', 'course', 'id')
        import_id_fields = ['first_name', 'last_name']

class TeacherResource(ModelResource):
    class Meta(object):
        model = GoogleUser
