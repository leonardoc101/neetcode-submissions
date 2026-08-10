# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(0)
        cur = out

        # base cases
        if not list1:
            cur.next = list2
            return out.next
        if not list2:
            cur.next = list1
            return out.next

        # recursive case
        if list1.val < list2.val:
            cur.next = ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            cur.next = ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        return out.next