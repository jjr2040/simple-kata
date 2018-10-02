from unittest import TestCase
import stats


class TestStats(TestCase):
    def test_calc_stats(self):
        result = stats.calc_stats("")
        a = [0]
        self.assertTrue(result == a)

