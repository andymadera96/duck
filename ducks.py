class Duck:

    #the __init__ is the Constructor( it build the duck essentially)
    def __init__(self, name, weight, color, sex):#Arguments we are passing to the duck class to initialize their attributes
        #These are the attributes to the Duck objects
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
    
    def displayInfo(self):
        print(self.name)
        print(self.weight)
        print(self.color)
        print(self.sex)
        print(self.isAlive)