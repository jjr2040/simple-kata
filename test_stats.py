from unittest import TestCase
from stats import Stats


class TestStats(TestCase):
    def test_calc_stats(self):
        stats = Stats()
        result = stats.calc_stats("1,10,8,4,12")
        a = [5]
        self.assertTrue(result == a)


