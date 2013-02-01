import sys
from fruitSimpleFactory import FruitSimpleFactory

if __name__ == "__main__":
    factory = FruitSimpleFactory()

    while True:
        try:
            print "-"*30
            fruitRaw = raw_input("Please input a fruit:\n")
        except:
            print "\nEnding Now, Thank you! ......"
            sys.exit()
        else:
            fruitStr = fruitRaw.strip()
        
        if fruitStr == "":
            continue
        else:
            fruitFactory = factory.createFruitFactory(fruitStr)
            fruitObj = fruitFactory.createFruit()
            fruitObj.getIntro()
            print ""
