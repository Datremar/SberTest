import unittest

from dogs import Dog


class DogTestCase(unittest.TestCase):
    def test_energy_consistency(self):
        dog = Dog('Test')
        e_before = dog.energy

        dog.say()
        dog.fly()

        self.assertTrue(e_before == dog.energy)

    def test_energy_after_run(self):
        dog = Dog('Test')
        e_before = dog.get_energy()

        dog.run()

        self.assertFalse(e_before == dog.get_energy())

    def test_energy_after_swim(self):
        dog = Dog('Test')
        e_before = dog.get_energy()

        dog.swim()

        self.assertFalse(e_before == dog.get_energy())