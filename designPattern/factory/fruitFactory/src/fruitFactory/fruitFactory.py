'''
Created on 2010-12-29

@author: wenxianw
'''

FRUIT_FILE_NAME = "fruit"
FRUIT_CLASS_NAME = "Fruit" 
FACTORY_CLASS_DIR = "fruitFactory"
FACTORY_CLASS_NAME = "fruitFactory"

class FruitFactory(object):
    def __init__(self):
        self.fruitClassDir = "fruitClass"
        
    def importFruitClass(self, fileName, className):
        importNameStr =  "%s.%s" % (self.fruitClassDir, fileName)
        if __name__ == "%s.%s" % (FACTORY_CLASS_DIR, FACTORY_CLASS_NAME):
            importNameStr = "%s.%s.%s" % (FACTORY_CLASS_DIR, self.fruitClassDir, fileName)
            
        fruitClassModule = __import__(name = importNameStr, fromlist = className)
        return fruitClassModule.__dict__[className]
    
    def createFruit(self):
        raise NotImplementedError("Not Subclass FruitFactory::createFruit()!");
    
if __name__ == "__main__":
    factory = FruitFactory()
    try:
        factory.createFruit()
    except NotImplementedError:
        print "Not Implement!"
        
