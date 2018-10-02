from unittest import TestCase
from stats import Stats


class TestStats(TestCase):
    def test_calc_stats(self):
        stats = Stats()
        result = stats.calc_stats("")
        a = [0]
        self.assertTrue(result == a)

