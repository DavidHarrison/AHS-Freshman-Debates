#!/usr/bin/env python2.7
#file: merge_debaters.py
#transform school-given student records to simple csv records for easy
#parsing into Django database

from csv      import DictReader, DictWriter
from tempfile import TemporaryFile

ENGLISH_COURSE_ID = u"10CP01"
IHS_COURSE_ID     = u"900012"
IN_FIELDS         = [u'name', u'period', u'teacher', u'course_id']
OUT_FIELDS        = [u'id', u'first_name', u'last_name', u'english_period',
                     u'english_teacher', u'ihs_period', u'ihs_teacher']

def mergeDebaters(f_old):
    debaters_old = list(DictReader(f_old, fieldnames=IN_FIELDS))
    english_debaters, ihs_debaters = [], []
    for d in debaters_old:
        if d[u'course_id'] == ENGLISH_COURSE_ID:
            english_debaters.append(d)
        elif d[u'course_id'] == IHS_COURSE_ID:
            ihs_debaters.append(d)
    debaters_new = []
    i = 0
    debaters_zipped = zipDebaters(english_debaters, ihs_debaters)
    debaters_zipped.reverse()
    for d in debaters_zipped:
        debater = splitName(d)
        debater['id'] = str(i)
        debaters_new.append(debater)
        i += 1
    return debaters_new
    #f_new = TemporaryFile()
    #for d in debaters_new:
    #    DictWriter(f_new, OUT_FIELDS).writerow(d)
    #return f_new

def zipDebaters(english, ihs):
    if len(english) > 0:
        e = english[0]
        possible_is = []
        for d in ihs:
            if d[u'name'] == e[u'name']:
                possible_is.append(d)
        if len(ihs) > 0 and len(possible_is) > 0:
            i = possible_is[0]
            new_ihs = []
            for d in ihs:
                if d[u'name'] != e[u'name']:
                    new_ihs.append(d)
            new_debater = mergeDebater(e, i)
        else:
            new_debater = mergeDebater(e, None)
            new_ihs = ihs
    else:
        if len(ihs) > 0:
            new_debater = mergeDebater(None, ihs[0])
            new_ihs = ihs[1:]
        else:
            return []
    debaters = zipDebaters(english[1:], new_ihs)
    debaters.append(new_debater)
    return debaters

def mergeDebater(english, ihs):
    debater = {}
    if english != None:
        debater[u'name']            = english[u'name']
        debater[u'english_period']  = english[u'period']
        debater[u'english_teacher'] = english[u'teacher']
    else:
        debater[u'name']            = None
        debater[u'english_period']  = None
        debater[u'english_teacher'] = None
    if ihs != None:
        debater[u'name']        = ihs['name']
        debater[u'ihs_period']  = ihs['period']
        debater[u'ihs_teacher'] = ihs['teacher']
    else:
        debater[u'ihs_period']  = None
        debater[u'ihs_teacher'] = None
    #if both english and ihs are null, return None
    if debater[u'name'] == None:
        return None
    #otherwise, return the constructed debater dict (may have None fields)
    return debater

def splitName(debater):
    name = debater[u'name']
    last_name  = name.split(u", ")[0]
    first_name = name.split(u", ")[1]
    debater.pop(u'name', None)
    debater[u'first_name'] = first_name
    debater[u'last_name']  = last_name
    return debater

'''
with open("freshmen.csv", 'r') as f:
    debaters = mergeDebaters(f)
with open("debaters.csv", 'w') as f:
    dw = DictWriter(f, OUT_FIELDS)
    dw.writeheader()
    for d in debaters:
        dw.writerow(d)
'''
