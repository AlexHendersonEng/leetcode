import unittest

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If number of rows is 1 return original string
        if numRows == 1: return s

        # Initialise row index, row delta and row array
        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        # Loop of letters in string
        for l in s:
            # Append letter to row array
            rows[idx].append(l)

            # If on first row set row delta to 1
            if idx == 0:
                d = 1
            # Else if on last row set row delta to -1
            elif idx == numRows - 1:
                d = -1

            # Change row index
            idx += d

        # Join rows together
        res = ""
        for row_i in range(numRows):
            res += ''.join(rows[row_i])

        # Return result
        return res
                    

class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        res = self.sol.convert("PAYPALISHIRING", 3)
        self.assertEqual(res, "PAHNAPLSIIGYIR")

    def test_case2(self):
        res = self.sol.convert("PAYPALISHIRING", 4)
        self.assertEqual(res, "PINALSIGYAHRPI")


if __name__ == "__main__":
    unittest.main()