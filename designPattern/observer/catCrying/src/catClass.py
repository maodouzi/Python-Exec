'''
Created on 2010-12-30

@author: wenxianw
'''

CAT_CRY_EVENT = "catCry"

class Cat(object):
    def __init__(self, nameStr):
        self.observerList = []
        self.nameStr = nameStr
        
    def register(self, observer):
        self.observerList.append(observer)
 
    def unregister(self, observer):
        self.observerList.remove(observer)
 
    def notifyAll(self, event):
        for observer in self.observerList:
            observer.notify(event)
    
    def cry(self):
        print ""
        print "-" * 30
        print "Cat %s start crying ..." % self.nameStr
        self.notifyAll("catCry")

if __name__ == '__main__':
    tomCat = Cat("Tom")
    tomCat.cry()