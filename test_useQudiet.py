from useQudiet import RUN_CIRC
import unittest

testcases = [
    [5, [1, 1, 1, 1, 1], '|11110>'],
    [6, [1, 1, 1, 1, 1, 1], '|111110>'],
    [7, [1, 1, 1, 1, 1, 1, 1], '|1111110>'],
    [5, [1, 0, 1, 1, 1], '|10111>'],
    [6, [1, 1, 1, 0, 0, 1], '|111001>'],
    [7, [0, 0, 0, 0, 1, 1, 1], '|0000111>'],
    [5, [0, 0, 0, 0, 0], '|00000>'],
    [6, [0, 0, 0, 0, 0, 1], '|000001>'],
    [10, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], '|1010101010>'],
    [8, [0, 0, 0, 0, 1, 1, 1, 1], '|00001111>'],
    [9, [1, 1, 1, 1, 1, 1, 0, 1, 0], '|111111010>'],
    [8, [0, 0, 0, 0, 0, 0, 0, 0], '|00000000>'],
    [11, [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], '|11111111000>'],
]


class TestingCircuit(unittest.TestCase):
    pass


def generateTest(n, inp, exp, testNo):
    def test(self):
        self.assertEqual(RUN_CIRC(n, inp), exp, f"Test Case #${testNo} fail")

    return test


if __name__ == '__main__':

    for index, (_n, _inp, _exp) in enumerate(testcases, start=1):
        test_name = f'test_case_${index}'
        current_test = generateTest(_n, _inp, _exp, index)
        setattr(TestingCircuit, test_name, current_test)
    unittest.main()
