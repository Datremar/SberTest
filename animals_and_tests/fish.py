from abstract_animal import Animal


class Fish(Animal):
    def swim(self):
        print(f"My name is {self.name} and i am swimming")
        self.energy = self.energy - 5


class FlyingFish(Fish):
    def fly(self):
        print("My name is " + str(self.name) + " and i flying")
        self.energy = self.energy - 20
