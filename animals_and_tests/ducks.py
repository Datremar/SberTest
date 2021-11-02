from abstract_animal import Animal


class Duck(Animal):
    def run(self):
        print(f"My name is {self.name} and i am running")
        self.energy = self.energy - 5

    def swim(self):
        print(f"My name is {self.name} and i am swimming")
        self.energy = self.energy - 10

    def fly(self):
        print(f"My name is {self.name} and i am flying")
        self.energy = self.energy - 30

