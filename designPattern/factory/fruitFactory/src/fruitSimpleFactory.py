'''
Created on 2010-12-29

@author: wenxianw
'''

import os, re
from fruitFactory.fruitFactoryUnknow import FruitFactoryUnknow

FRUIT_CLASS_DIR = "fruitFactory"

class FruitSimpleFactory(object):
    def __init__(self):
        fruitReg = re.compile("^(fruitFactory_(.+))\.py$")
        fruitsList = [fruitReg.match(fruitStr).groups() for fruitStr in os.listdir(FRUIT_CLASS_DIR) if fruitReg.match(fruitStr)]
        # print fruitsList
    
        self.fruitMoDict = {}
        for fruitMoName in fruitsList:
            self.fruitMoDict[fruitMoName[1].capitalize()] = __import__(name = "%s.%s" % (FRUIT_CLASS_DIR, fruitMoName[0]), fromlist = ["%sFactory" % fruitMoName[1].capitalize()])
        
    def createFruitFactory(self, fruitStr):
        fruitName = fruitStr.lower().capitalize()        
    
        if fruitName in self.fruitMoDict:
            return self.fruitMoDict[fruitName].__dict__["%sFactory" % fruitName]()
        else:
            return FruitFactoryUnknow(fruitStr)
    
if __name__ == "__main__":
    simpleFactory = FruitSimpleFactory()
    factory = simpleFactory.createFruitFactory("appLe")
    fruitObj = factory.createFruit()
    fruitObj.getIntro()
    
    factory = simpleFactory.createFruitFactory("orange")
    fruitObj = factory.createFruit()
    fruitObj.getIntro()
