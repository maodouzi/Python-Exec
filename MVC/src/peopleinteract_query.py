'''
Created on 2011-7-22

@author: wenxianw
'''

# interactive queries
import shelve
fieldnames = (('name', str), ('age', int), ('job', str), ('pay', float))
maxfield   = max(len(f) for (f, t) in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = raw_input('\nKey? => ')       # key or empty line, exc at eof
    if not key: break
    try:
        record = db[key]                # fetch by key, show in console
    except:
        print 'No such key "%s"!' % key
    else:
        for (field, fieldType) in fieldnames:
            print field.ljust(maxfield), '=>', getattr(record, field)


 

