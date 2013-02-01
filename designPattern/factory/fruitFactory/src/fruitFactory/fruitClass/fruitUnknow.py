'''
Created on 2010-12-29

@author: wenxianw
'''

from fruit import Fruit

class FruitUnknow(Fruit):
    '''
    For unknow fruit.
    '''


    def __init__(self, fruitName):
        Fruit.__init__(self)
        self.fruitName = fruitName
    
    def getIntro(self):
        print "Unknow the fruit: %s!" % self.fruitName

if __name__ == "__main__":
    FruitUnknow("apple").getIntro()
        