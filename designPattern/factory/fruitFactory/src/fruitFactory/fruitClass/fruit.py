class Fruit(object):
    def __init__(self):
        print "Constructor of %s ..." % self.__class__.__name__
    
    def getIntro(self):
        print "Fruit is good for health!"

if __name__ == "__main__":
    Fruit().getIntro()
    
