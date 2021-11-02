from abc import ABC, abstractmethod


class AbstractAnimal(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Animal(AbstractAnimal):
    def __init__(self, name: str, energy=100):
        if type(name) is not str:
            raise TypeError(f'Wrong name type {type(name)}. Should be str instead.')
        if type(energy) not in [float, int]:
            raise TypeError(f'Wrong energy type {type(energy)}. Should be float or int instead.')

        self.name = name
        self.energy = energy

    def say(self):
        print(f"Hello, i'm {self.__class__.__name__} and my name is {self.name}")

    def swim(self):
        print(f"My name is {self.name} and i can't swim")

    def fly(self):
        print(f"My name is {self.name} and i can't fly")

    def run(self):
        print(f"My name is {self.name} and i can't run")

    def get_energy(self):
        return self.energy

