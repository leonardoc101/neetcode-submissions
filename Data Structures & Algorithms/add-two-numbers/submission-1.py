# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, None)
        prev = result
        cur = None
        carry_over = False

        while l1 is not None or l2 is not None or carry_over:
            # add dummy 0 nodes
            if l1 is None:
                l1 = ListNode(0, None)
            if l2 is None:
                l2 = ListNode(0, None)

            # carry the 1
            if carry_over:
                added = l1.val + l2.val + 1
            else:
                added = l1.val + l2.val

            # make a new node with the correct value and link it
            cur = ListNode(added % 10, None)
            prev.next = cur

            # safe since all are guaranteed to not be None
            prev = prev.next
            l1 = l1.next
            l2 = l2.next

            # carry the 1 if the sum is greater than 10
            if added >= 10:
                carry_over = True
            else:
                carry_over = False

        # both lists end but carry over must occur
        return result.next