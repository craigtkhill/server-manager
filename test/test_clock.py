import unittest
from src.clock import Clock


class TestClock(unittest.TestCase):
    def test_init(self):
        clock = Clock()
        self.assertIsNotNone(clock)

    def test_tick(self):
        clock = Clock()
        clock.tick(1)
        self.assertEqual(clock.get_time(), 1)

    def test_get_time(self):
        clock = Clock()
        self.assertEqual(clock.get_time(), 0)

    def test_reset(self):
        clock = Clock()
        clock.tick()
        clock.reset()
        self.assertEqual(clock.get_time(), 0)

    def test_tick_random(self):
        clock = Clock()
        clock.tick_random(lower_bound=1, upper_bound=3)
        self.assertGreaterEqual(clock.get_time(), 1)
        self.assertLessEqual(clock.get_time(), 100)
