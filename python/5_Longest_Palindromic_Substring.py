import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialise result variables
        res = ""
        resLen = 0

        # Loop through letters in string
        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Check if new longest palindrome has been found
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = len(res)

                # Move left and right pointers
                l -= 1
                r += 1

            # Odd length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Check if new longest palindrome has been found
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = len(res)

                # Move left and right pointers
                l -= 1
                r += 1

        # Return result
        return res
                    

class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        res = self.sol.longestPalindrome("babad")
        self.assertEqual(res, "bab")

    def test_case2(self):
        res = self.sol.longestPalindrome("cbbd")
        self.assertEqual(res, "bb")


if __name__ == "__main__":
    unittest.main()