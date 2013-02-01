'''
Created on 2010-12-30

@author: wenxianw
'''

from fruitFactory import FruitFactory

FRUIT_FILE_NAME = "fruit_pear"
FRUIT_CLASS_NAME = "Pear" 

class PearFactory(FruitFactory):
    def __init__(self):
        FruitFactory.__init__(self)
        self.fruitClass = self.importFruitClass(FRUIT_FILE_NAME, FRUIT_CLASS_NAME)
    
    def createFruit(self):
        print "Ready to create %s" % FRUIT_CLASS_NAME
        return self.fruitClass()

if __name__ == '__main__':
    factory = PearFactory()
    fruitObj = factory.createFruit()
    fruitObj.getIntro()