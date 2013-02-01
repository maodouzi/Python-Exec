import fruit

class Banana(fruit.Fruit):
    def getIntro(self):
        print "Banana is good for health!"

if __name__ == "__main__":
    Banana().getIntro()
