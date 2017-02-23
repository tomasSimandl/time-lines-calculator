import unittest
import data_reading.reading as reader


class TestReader(unittest.TestCase):

    def test_time_convert(self):
        # success tests
        input_params = [
            ['123', reader.time_definition['s'], 123],
            ['123456789', reader.time_definition['ms'], 123456],
            ['123456789', reader.time_definition['us'], 123],
            ['10:20:10 2.5.2010', '%H:%M:%S %d.%m.%Y', 1272788410],
            ['0', reader.time_definition['us'], 0],
            ['-10', reader.time_definition['s'], -10],
        ]

        for date in input_params:
            self.assertEqual(reader.time_convert(date[0], date[1]).timestamp(), date[2])

        # failure tests
        self.assertRaises(ValueError, reader.time_convert, 'bad text', '%H %M')
        self.assertRaises(ValueError, reader.time_convert, 'bad text', 'seconds')


if __name__ == '__main__':
    unittest.main()
