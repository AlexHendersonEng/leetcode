import unittest

class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading whitespace
        res = s.lstrip()

        # Return 0 if the string is empty
        if not res:
            return 0

        # Determine the sign of the number
        match res[0]:
            case '-':
                is_negative = True
                res = res[1:]
            case '+':
                is_negative = False
                res = res[1:]
            case _:
                is_negative = False

        # Find non-digit character
        for i in range(len(res)):
            if not res[i].isdigit():
                res = res[:i]
                break

        # Check for overflow and underflow
        try:
            if is_negative:
                if int(res) > 2**31:
                    return -2**31
                return -int(res)
            else:
                if int(res) > 2**31 - 1:
                    return 2**31 - 1
                return int(res)
        except:
            return 0


class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        res = self.sol.myAtoi("42")
        self.assertEqual(res, 42)

    def test_case2(self):
        res = self.sol.myAtoi("-042")
        self.assertEqual(res, -42)

    def test_case3(self):
        res = self.sol.myAtoi("1337c0d3")
        self.assertEqual(res, 1337)

    def test_case4(self):
        res = self.sol.myAtoi("0-1")
        self.assertEqual(res, 0)

    def test_case5(self):
        res = self.sol.myAtoi("words and 987")
        self.assertEqual(res, 0)


if __name__ == "__main__":
    unittest.main()