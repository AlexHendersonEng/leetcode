import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert integer to string
        x_str = str(x)
        
        # Setup pointers
        lp, rp = 0, len(x_str) - 1

        # Move pointer towards each other
        while lp < rp:
            # If the characters are not equal, return False
            if x_str[lp] != x_str[rp]:
                return False

            # Move pointers
            lp += 1
            rp -= 1

        # Number is palindrome
        return True


class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        res = self.sol.isPalindrome(121)
        self.assertEqual(res, True)

    def test_case2(self):
        res = self.sol.isPalindrome(-121)
        self.assertEqual(res, False)

    def test_case3(self):
        res = self.sol.isPalindrome(10)
        self.assertEqual(res, False)


if __name__ == "__main__":
    unittest.main()