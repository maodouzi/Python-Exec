'''
Created on 2010-12-30

@author: wenxianw
'''

from catClass import Cat
from absCatCryObserver import AbsCatCryObserver

class Human(AbsCatCryObserver):
    
    def catCryHandle(self):
        print "%s wake up!" % self.nameStr

if __name__ == '__main__':
    tomCat = Cat("Tom")
    hostessGreen = Human("Mrs Green")
    hostessGreen.registerTo(tomCat)
    tomCat.cry()