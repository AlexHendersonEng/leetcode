import unittest

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure binary search is run on smallest array
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        # Get total and half list length
        total = len(A) + len(B)
        half = total // 2

        # Setup pointer
        l, r = 0, len(A) - 1

        while True:
            # Get middle indexes
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            # Get comparison values
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd
                if total % 2:
                    return min(Aright, Bright)
                
                # Even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # Move right pointer
            elif Aleft > Bright:
                r = i - 1
            # Move left pointer
            else:
                l = i + 1
                    

class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        res = self.sol.findMedianSortedArrays([1, 3], [2])
        self.assertEqual(res, 2)

    def test_case2(self):
        res = self.sol.findMedianSortedArrays([1, 2], [3, 4])
        self.assertEqual(res, 2.5)


if __name__ == "__main__":
    unittest.main()