import unittest

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Get list length
        n_nums = len(nums)

        # Loop over nums index's
        for idx1 in range(n_nums):

            # Loop over nums index's
            for idx2 in range(n_nums):

                # Break condition
                if idx2 <= idx1: continue

                # Return if value attained
                if (nums[idx1] + nums[idx2]) == target:
                    return [idx1, idx2]
                    
class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        res = self.sol.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(res, [0, 1])

    def test_case2(self):
        res = self.sol.twoSum([3, 2, 4], 6)
        self.assertEqual(res, [1, 2])

    def test_case3(self):
        res = self.sol.twoSum([3, 3], 6)
        self.assertEqual(res, [0, 1])


if __name__ == "__main__":
    unittest.main()