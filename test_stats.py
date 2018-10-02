from unittest import TestCase
from stats import Stats


class TestStats(TestCase):
    def test_calc_stats(self):
        stats = Stats()
        result = stats.calc_stats("")
        a = [0, 0, 0, 0]
        self.assertTrue(result == a, msg="Cuando string llega vacio")
        result = stats.calc_stats("1")
        a = [1, 1, 1, 1]
        self.assertTrue(result == a,  msg="Cuando hay 1 elemento en el string")
        result = stats.calc_stats("1,10")
        a = [2, 1, 10, 5.5]
        self.assertTrue(result == a, msg="Cuando hay 2 elemento en el string")
        result = stats.calc_stats("1,10,8,4,12")
        a = [5, 1, 12, 7]
        self.assertTrue(result == a, msg="Cuando hay n elemento en el string")



