'''
Created on 2010-12-30

@author: wenxianw
'''

from catClass import Cat
from mouseClass import Mouse
from humanClass import Human

if __name__ == '__main__':
    tomCat = Cat("Tom")
    
    mouseJerry = Mouse("Jerry")
    mouseJerry.registerTo(tomCat)
    
    hostessGreen = Human("Mrs Green")
    hostessGreen.registerTo(tomCat)
    
    tomCat.cry()
    
    hostessGreen.unregisterTo(tomCat)
    
    tomCat.cry()