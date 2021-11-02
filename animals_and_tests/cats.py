from abstract_animal import Animal


class Cat(Animal):
    def run(self):
        print(f"My name is {self.name} and i am running")
        self.energy = self.energy - 5


class Tiger(Animal):
    def run(self):
        print(f"My name is {self.name} and i am running")
        self.energy = self.energy - 20

    def swim(self):
        print(f"My name is {self.name} and i am swimming")
        self.energy = self.energy - 40

