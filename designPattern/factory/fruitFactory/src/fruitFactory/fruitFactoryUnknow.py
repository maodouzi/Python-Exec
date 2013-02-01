'''
Created on 2010-12-30

@author: wenxianw
'''

from fruitFactory import FruitFactory

FRUIT_FILE_NAME = "fruitUnknow"
FRUIT_CLASS_NAME = "FruitUnknow" 

class FruitFactoryUnknow(FruitFactory):
    def __init__(self, fruitStr):
        FruitFactory.__init__(self)
        self.fruitStr = fruitStr
        self.fruitClass = self.importFruitClass(FRUIT_FILE_NAME, FRUIT_CLASS_NAME)
    
    def createFruit(self):
        print "Ready to create %s" % FRUIT_CLASS_NAME
        return self.fruitClass(self.fruitStr)

if __name__ == '__main__':
    factory = FruitFactoryUnknow("orange")
    fruitObj = factory.createFruit()
    fruitObj.getIntro()