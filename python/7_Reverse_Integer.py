import unittest

class Solution:
    def reverse(self, x: int) -> int:
        # Conver integer to string
        num_str = str(x)

        # Check if the number is negative
        if num_str[0] == '-':
            res = '-' + num_str[1:][::-1]
        else:
            res = num_str[::-1]

        # Return string converted to integer
        return int(res) if -2**31 <= int(res) <= 2**31 - 1 else 0


class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        res = self.sol.reverse(123)
        self.assertEqual(res, 321)

    def test_case2(self):
        res = self.sol.reverse(-123)
        self.assertEqual(res, -321)

    def test_case3(self):
        res = self.sol.reverse(120)
        self.assertEqual(res, 21)


if __name__ == "__main__":
    unittest.main()