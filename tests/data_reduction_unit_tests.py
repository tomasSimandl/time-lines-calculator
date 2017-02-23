import unittest
import calculations.data_reduction as reductor
from datetime import datetime, timedelta


class TestDataReduction(unittest.TestCase):

    def test_reduct_empty_list(self):
        self.assertSequenceEqual(reductor.reduct([], self.dt(1), self.dt(1), self.td(1)), [])

    def test_reduct_invalid_list(self):
        input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(10), self.dt(100), self.td(20)), [])

        input_list = [[11, 'a'], [12, 'c']]
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(10), self.dt(100), self.td(100)), [])

        input_list = [[self.dt(11), 12], [self.dt(13), 14]]
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(1), self.dt(100), self.td(1)), [])

    def test_reduct_invalid_time(self):
        input_list = [
            [self.dt(1), 123],
            [self.dt(11), 122],
            [self.dt(21), 124],
            [self.dt(31), 131],
            [self.dt(41), 90],
            [self.dt(51), 120]
        ]
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(20), self.dt(10), self.td(1)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(11), self.dt(11), self.td(1)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(11), self.dt(11), self.td(0)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(-1), self.dt(20), self.td(10)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(-1), self.dt(-20), self.td(10)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(1), self.dt(20), self.td(-10)), [])

    def test_reduct_success(self):
        input_list = [
            (self.dt(1), 123),
            (self.dt(11), 122),
            (self.dt(21), 124),
            (self.dt(31), 131),
            (self.dt(41), 100),
            (self.dt(51), 180)
        ]
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(10), self.dt(20), self.td(10)), [(self.dt(10), 122)])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(10), self.dt(11), self.td(10)), [(self.dt(10), 122)])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(10), self.dt(21), self.td(10)), [(self.dt(10), 122), (self.dt(20), 124)])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(50), self.dt(60), self.td(2)), [(self.dt(50), 180)])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(0), self.dt(100), self.td(100)), [(self.dt(0), 130)])
        self.assertSequenceEqual(reductor.reduct(input_list, self.dt(0), self.dt(100), self.td(50)), [(self.dt(0), 120), (self.dt(50), 180)])

    def dt(self, time):
        return datetime.fromtimestamp(time)

    def td(self, time):
        return timedelta(seconds=time)

if __name__ == '__main__':
    unittest.main()