# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        NL = ListNode(0, None)
        # base cases: one list is empty
        if not list1:
            return list2
        if not list2:
            return list1
        # recursive case: compare value
        if list1.val > list2.val:
            NL.val = list2.val
            NL.next = self.mergeTwoLists(list1, list2.next)
        else:
            NL.val = list1.val
            NL.next = self.mergeTwoLists(list1.next, list2)
        return NL



                