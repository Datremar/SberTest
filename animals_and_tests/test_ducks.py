import unittest

from ducks import Duck


class DuckTestCase(unittest.TestCase):
    def test_energy_consistency(self):
        duck = Duck('Test')
        e_before = duck.energy

        duck.say()

        self.assertTrue(e_before == duck.energy)

    def test_energy_after_run(self):
        duck = Duck('Test')
        e_before = duck.get_energy()

        duck.run()

        self.assertFalse(e_before == duck.get_energy())

    def test_energy_after_swim(self):
        duck = Duck('Test')
        e_before = duck.get_energy()

        duck.swim()

        self.assertFalse(e_before == duck.get_energy())

    def test_energy_after_fly(self):
        duck = Duck('Test')
        e_before = duck.get_energy()

        duck.fly()

        self.assertFalse(e_before == duck.get_energy())