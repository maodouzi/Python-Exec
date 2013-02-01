'''
Created on 2010-12-29

@author: wenxianw
'''

import os, re
from fruitClass.fruitUnknow import FruitUnknow

FRUIT_CLASS_DIR = "fruitClass"

class FruitFactory(object):
    def __init__(self):
        fruitReg = re.compile("^(fruit_(.+))\.py$")
        fruitsList = [fruitReg.match(fruitStr).groups() for fruitStr in os.listdir(FRUIT_CLASS_DIR) if fruitReg.match(fruitStr)]
        #print fruitsList
    
        self.fruitMoDict = {}
        for fruitMoName in fruitsList:
            self.fruitMoDict[fruitMoName[1].capitalize()] = __import__(name = "%s.%s" % (FRUIT_CLASS_DIR, fruitMoName[0]), fromlist = [fruitMoName[1].capitalize()])
        #print fruitMoDict
        
    def createFruit(self, fruitStr):
        fruitName = fruitStr.lower().capitalize()        
    
        if fruitName in self.fruitMoDict:
            return self.fruitMoDict[fruitName].__dict__[fruitName]()
        else:
            return FruitUnknow(fruitStr)
    
if __name__ == "__main__":
    fruitFactory = FruitFactory()
    appleObj = fruitFactory.createFruit("appLe")
    appleObj.getIntro()
    orangeObj = fruitFactory.createFruit("orange")
    orangeObj.getIntro()