
class Ninja:
    def __init__(self,name,last_name,pet,reward,pet_food):
        self.name = name
        self.last_name = last_name
        self.pet = pet
        self.reward = reward
        self.pet_food = pet_food
        

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bath(self):
        self.pet.noise()

import petmascota



class subPet(petmascota.Pet):
    def __init__(self,name,type,candies,noise,size,color,age):
        super().__init__(name,type,candies,noise)
        self.size = size
        self.color = color
        self.age = age
    def moverCola(self):
        if self.candies == "banana":
            print("")
        



naruto = Ninja("Naruto","Uzumaki",petmascota.jack,"bone","meat")
naruto.feed().walk()
print(petmascota.jack.health)
