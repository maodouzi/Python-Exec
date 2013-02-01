'''
Created on 2010-12-30

@author: wenxianw
'''

from catClass import Cat
from catClass import CAT_CRY_EVENT

class AbsCatCryObserver(object):
    def __init__(self, nameStr):
        self.nameStr = nameStr

    def registerTo(self, subject):
        print "%s register to %s" % (self.nameStr, subject.nameStr)
        subject.register(self)
        
    def unregisterTo(self, subject):
        print "%s unregister to %s" % (self.nameStr, subject.nameStr)
        subject.unregister(self)
    
    def notify(self, event):
        print "%s was notified with the event: %s" % (self.nameStr, event)
        if event == CAT_CRY_EVENT:
            self.catCryHandle()
    
    def catCryHandle(self):
        raise NotImplementedError("Not implement AbsCatCryObserver::catCryHandle!");

if __name__ == '__main__':
    tomCat = Cat("Tom")
    observer = AbsCatCryObserver("Jerry")
    observer.registerTo(tomCat)
    try:
        tomCat.cry()
    except NotImplementedError:
        print "Not implement AbsCatCryObserver::catCryHandle!"