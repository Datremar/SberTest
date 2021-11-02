import unittest

from cats import Cat, Tiger


class CatTestCase(unittest.TestCase):
    def test_energy_consistency(self):
        cat = Cat('Test')

        e_before = cat.energy

        cat.say()
        cat.fly()
        cat.swim()

        self.assertTrue(e_before == cat.energy)

    def test_energy_after_run(self):
        cat = Cat('Test')
        e_before = cat.get_energy()

        cat.run()

        self.assertFalse(e_before == cat.get_energy())


class TigerTestCase(unittest.TestCase):
    def test_energy_consistency(self):
        tiger = Tiger('Test')
        e_before = tiger.energy

        tiger.say()
        tiger.fly()

        self.assertTrue(e_before == tiger.energy)

    def test_energy_after_run(self):
        tiger = Tiger('Test')
        e_before = tiger.get_energy()

        tiger.run()

        self.assertFalse(e_before == tiger.get_energy())

    def test_energy_after_swim(self):
        tiger = Tiger('Test')
        e_before = tiger.get_energy()

        tiger.swim()

        self.assertFalse(e_before == tiger.get_energy())
