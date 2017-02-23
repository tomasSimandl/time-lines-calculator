import unittest
import calculations.data_reduction as reductor
from datetime import datetime, timedelta


def dt(time):
    return datetime.fromtimestamp(time)


def td(time):
    return timedelta(seconds=time)


class TestDataReduction(unittest.TestCase):
    def test_reduct_empty_list(self):
        self.assertSequenceEqual(reductor.reduct([], dt(1), dt(1), td(1)), [])

    def test_reduct_invalid_list(self):
        input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        self.assertSequenceEqual(reductor.reduct(input_list, dt(10), dt(100), td(20)), [])

        input_list = [[11, 'a'], [12, 'c']]
        self.assertSequenceEqual(reductor.reduct(input_list, dt(10), dt(100), td(100)), [])

        input_list = [[dt(11), 12], [dt(13), 14]]
        self.assertSequenceEqual(reductor.reduct(input_list, dt(1), dt(100), td(1)), [])

    def test_reduct_invalid_time(self):
        input_list = [
            [dt(1), 123],
            [dt(11), 122],
            [dt(21), 124],
            [dt(31), 131],
            [dt(41), 90],
            [dt(51), 120]
        ]
        self.assertSequenceEqual(reductor.reduct(input_list, dt(20), dt(10), td(1)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(11), dt(11), td(1)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(11), dt(11), td(0)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(-1), dt(20), td(10)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(-1), dt(-20), td(10)), [])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(1), dt(20), td(-10)), [])

    def test_reduct_success(self):
        input_list = [
            [dt(1), 123],
            [dt(11), 122],
            [dt(21), 124],
            [dt(31), 131],
            [dt(41), 100],
            [dt(51), 180]
        ]
        self.assertSequenceEqual(reductor.reduct(input_list, dt(10), dt(20), td(10)), [[dt(10), 122]])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(10), dt(11), td(10)), [[dt(10), 122]])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(10), dt(21), td(10)), [[dt(10), 122], [dt(20), 124]])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(50), dt(60), td(2)), [[dt(50), 180]])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(0), dt(100), td(100)), [[dt(0), 130]])
        self.assertSequenceEqual(reductor.reduct(input_list, dt(0), dt(100), td(50)), [[dt(0), 120], [dt(50), 180]])

    def test_time_shift_plus(self):
        input_list = [
            [dt(1), 123],
            [dt(11), 122],
            [dt(21), 124],
            [dt(31), 131],
            [dt(41), 100],
            [dt(51), 180]
        ]

        expected_list = [
            [dt(11), 123],
            [dt(21), 122],
            [dt(31), 124],
            [dt(41), 131],
            [dt(51), 100],
            [dt(61), 180]
        ]

        self.assertSequenceEqual(reductor.time_shift(input_list, 10), expected_list)

    def test_time_shift_minus(self):
        input_list = [
            [dt(1), 123],
            [dt(11), 122],
            [dt(21), 124],
            [dt(31), 131],
            [dt(41), 100],
            [dt(51), 180]
        ]

        expected_list = [
            [dt(-9), 123],
            [dt(1), 122],
            [dt(11), 124],
            [dt(21), 131],
            [dt(31), 100],
            [dt(41), 180]
        ]

        self.assertSequenceEqual(reductor.time_shift(input_list, -10), expected_list)

    def test_time_shift_zero(self):
        input_list = [
            [dt(1), 123],
            [dt(11), 122],
            [dt(21), 124],
            [dt(31), 131],
            [dt(41), 100],
            [dt(51), 180]
        ]

        expected_list = [
            [dt(1), 123],
            [dt(11), 122],
            [dt(21), 124],
            [dt(31), 131],
            [dt(41), 100],
            [dt(51), 180]
        ]

        self.assertSequenceEqual(reductor.time_shift(input_list, 0), expected_list)

    def test_time_shift_invalid_list(self):
        input_list = [
            [dt(1), 123],
            [11, 122],
            [dt(21), 124],
            [dt(31), 131],
            [dt(41), 100],
            [dt(51), 180]
        ]

        expected_list = [
            [dt(1), 123],
            [11, 122],
            [dt(21), 124],
            [dt(31), 131],
            [dt(41), 100],
            [dt(51), 180]
        ]

        self.assertSequenceEqual(reductor.time_shift(input_list, 10), expected_list)


if __name__ == '__main__':
    unittest.main()
