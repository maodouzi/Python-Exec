'''
Created on 2011-7-22

@author: wenxianw
'''

# interactive updates
import shelve
from people import Person
fieldnames = (('name', str), ('age', int), ('job', str), ('pay', float))

db = shelve.open('class-shelve')
while True:
    key = raw_input('\nKey? => ')
    if not key: break
    if key in db.keys( ):
        record = db[key]                      # update existing record
    else:                                     # or make/store new rec
        record = Person(name='?', age='?')    # eval: quote strings
    for (field, fieldType) in fieldnames:
        currval = getattr(record, field)
        newtext = raw_input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, fieldType(newtext))
    db[key] = record
db.close( )
