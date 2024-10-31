import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialise variables
        best = 0

        # Loop over letters in string
        for i1 in range(0, len(s), 1):

            # Initialise variables
            curr = ""
            
            # Loop over letters in string
            for i2 in range(i1, len(s), 1):
            
                # Add letter to substring if not in current else break
                if s[i2] not in curr:
                    curr += s[i2]
                else:
                    break

            # Update best if required
            curr_ln = len(curr)
            if curr_ln > best:
                best = curr_ln
        
        # Return longest substring found
        return best
                    
class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        res = self.sol.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(res, 3)

    def test_case2(self):
        res = self.sol.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(res, 1)

    def test_case3(self):
        res = self.sol.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(res, 3)

if __name__ == "__main__":
    unittest.main()