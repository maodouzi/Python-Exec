'''
Created on 2010-12-30

@author: wenxianw
'''
from catClass import Cat
from absCatCryObserver import AbsCatCryObserver

class Mouse(AbsCatCryObserver):
    
    def catCryHandle(self):
        print "%s run to hole!" % self.nameStr

if __name__ == '__main__':
    tomCat = Cat("Tom")
    mouseJerry = Mouse("Jerry")
    mouseJerry.registerTo(tomCat)
    tomCat.cry()