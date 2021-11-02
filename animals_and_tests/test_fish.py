import unittest

from fish import Fish, FlyingFish


class FishTestCase(unittest.TestCase):
    def test_energy_consistency(self):
        fish = Fish('Test')
        e_before = fish.energy

        fish.say()
        fish.run()
        fish.fly()

        self.assertTrue(e_before == fish.energy)

    def test_energy_after_swim(self):
        fish = Fish('Test')
        e_before = fish.get_energy()

        fish.swim()

        self.assertFalse(e_before == fish.get_energy())


class FlyingFishTestCase(unittest.TestCase):
    def test_energy_consistency(self):
        fish = FlyingFish('Test')
        e_before = fish.energy

        fish.say()
        fish.run()

        self.assertTrue(e_before == fish.energy)

    def test_energy_after_fly(self):
        fish = FlyingFish('Test')
        e_before = fish.get_energy()

        fish.fly()

        self.assertFalse(e_before == fish.get_energy())
