import sys
from fruitFactory import FruitFactory

if __name__ == "__main__":
    factory = FruitFactory()

    while True:
        try:
            print "-"*30
            fruitRaw = raw_input("Please input a fruit:\n")
        except:
            print "\nEnding Now, Thank you! ......"
            sys.exit()
        else:
            fruitStr = fruitRaw.strip()
        
        if fruitStr.strip() == "":
            continue
        else:
            fruitObj = factory.createFruit(fruitStr)
            fruitObj.getIntro()
            print ""
