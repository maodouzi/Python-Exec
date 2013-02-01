import fruit

class Pear(fruit.Fruit):
    def getIntro(self):
        print "Pear is good for health!"

if __name__ == "__main__":
    Pear().getIntro()
