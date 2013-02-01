import fruit

class Apple(fruit.Fruit):
    def getIntro(self):
        print "Apple is good for health!"

if __name__ == "__main__":
    Apple().getIntro()
