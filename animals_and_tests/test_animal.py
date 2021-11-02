import unittest

from abstract_animal import Animal


class AnimalTestCase(unittest.TestCase):
    def test_name(self):
        for name in [-10, 10, 1 + 5j, 1.61, True, 'Test']:
            if type(name) is not str:
                with self.assertRaises(TypeError):
                    Animal(
                        name=name
                    )
            else:
                self.assertTrue(type(Animal(name).name) is str)

    def test_energy(self):
        for energy in [1, 0, -1, 1.61, 'energy', 1 + 5j, 10000000000000000]:
            if type(energy) not in [float, int]:
                with self.assertRaises(TypeError):
                    Animal(
                        name='Test',
                        energy=energy
                    )

            else:
                animal = Animal(name='Test', energy=energy)
                self.assertTrue(type(animal.energy) in [float, int])

            self.assertTrue(Animal(name='Test').energy == 100)

    def test_energy_consistency(self):
        animal = Animal('Test')

        e_before = animal.energy

        animal.say()
        animal.fly()
        animal.swim()
        animal.run()

        self.assertTrue(e_before == animal.energy)
