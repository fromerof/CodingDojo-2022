class Pet():
    def __init__(self,name,type,candies,noise):
        self.name = name
        self.type = type
        self.candies = candies
        self.noise = noise
        self.health = 100
        self.energy = 10
        
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.noise)

jack = Pet("Jack","Dog","Banana","puffpuff")
