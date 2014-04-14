#!/usr/bin/env python2.7
#file resources.py

from import_export.resources import ModelResource
from import_export.fields    import Field
from debates.models          import Student, GoogleUser
from debates.merge_debaters  import mergeDebaters
from logging                 import getLogger

logger = getLogger('logview.debugger')

#TODO, use inbuilt functions
class StudentResource(ModelResource):
    #CSV Fields
    name      = Field(column_name='Student Name', readonly=True)
    period    = Field(column_name='Period',       readonly=True)
    teacher   = Field(column_name='Teacher.',     readonly=True)
    course_id = Field(column_name='Course.',      readonly=True)
    
    def before_import(self, dataset, dry_run):
        #assignment of .dict needed to carry data over into calling function
        dataset.dict = mergeDebaters(dataset).dict

    #TODO, figure out what wasn't working about using the inbuilt version
    def get_instance(self, instance_loader, row):
        args = {}
        for key in self.get_import_id_fields():
            args[key] = row[key]
        matches = Student.objects.filter(**args)
        if len(matches) == 0:
            return None
        return matches[0]

    #TODO, should this be user-defined?
    def init_instance(self, row):
        return Student(**row)

    class Meta(object):
        model = Student
        #fields = ('first_name','last_name',
        #          'english_period','english_teacher',
        #          'ihs_period','ihs_teacher'
        exclude = ('Student Name', 'period', 'teacher', 'course', 'id')
        import_id_fields = ['first_name', 'last_name']

class TeacherResource(ModelResource):
    #TODO, may be able to import directly
    def before_import(dataset, dry_run):
        for t in dataset:
            teacher              = GoogleUser()
            teacher.first_name   = dictionary['first name']
            teacher.last_name    = dictionary['last name']
            teacher.role         = 1
            teacher.email        = dictionary['email']
            #TODO, figure out proper way to use password for teachers
            teacher.password     = "p_word"
            teacher.is_admin     = False
            teacher.is_staff     = True
            teacher.is_superuser = False
            if not dry_run:
                teacher.save()

    class Meta(object):
        model = GoogleUser
