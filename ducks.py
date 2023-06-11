class Duck: 

    #the __init__  is the Constructor (it builds our objects)
    def __init__(self, name, weight, color, sex): #Arguments we are passing to duck class to initalize their atrributes
        #These are the attributes to the Duck Objects
        self.name = name
        self.weight = weight
        self.color = color
        self.sex = sex
        self.isAlive = True

    def quack(self):
        print("Quack")

    def jump(self):
        print("boing")

    def eat(self):
        self.weight += 1

    def displaysInfo(self):
        print(self.name)
        print(self.weight)
        print(self.color)
        print(self.sex)
        print(self.isAlive)
