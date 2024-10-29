import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialise values
        carry = 0
        init = ListNode()
        l3 = init

        # Loop over linked list until both hit None node
        while l1 or l2 or carry:
            # Extract digits
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            # Add digits
            d = d1 + d2 + carry
            carry = d // 10
            l3.next = ListNode(d % 10)

            # Update pointers
            l3 = l3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return singley linked list
        return init.next

class TestCases(unittest.TestCase):
    sol = Solution()

    def test_case1(self):
        l1 = list_to_linked([2, 4, 3])

        l2 = list_to_linked([5, 6, 4])

        l3 = list_to_linked([7, 0, 8])

        res = self.sol.addTwoNumbers(l1, l2)
        self.assertTrue(compare_linked(res, l3))

    def test_case2(self):
        l1 = ListNode(0)

        l2 = ListNode(0)

        l3 = ListNode(0)

        res = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(res.val, l3.val)

    def test_case3(self):
        l1 = list_to_linked([9] * 7)

        l2 = list_to_linked([9] * 4)

        l3 = list_to_linked([8, 9, 9, 9, 0, 0, 0, 1])

        res = self.sol.addTwoNumbers(l1, l2)
        self.assertTrue(compare_linked(res, l3))

def list_to_linked(list: list[int]):
    # Initialise linked list
    linked = ListNode()
    pointer = linked

    # Loop over list
    for item in list:
        pointer.next = ListNode(item)
        pointer = pointer.next
    
    # Return linked list
    return linked.next

def compare_linked(l1, l2):
    # Loop through list (lists should be of same length)
    while l1:
        # Compare list values
        if l1.val != l2.val:
            return False

        # Step linked list pointers
        l1 = l1.next
        l2 = l2.next

    # Return true if no differences found
    return True

if __name__ == "__main__":
    unittest.main()