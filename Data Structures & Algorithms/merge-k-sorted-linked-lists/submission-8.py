# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.setrecursionlimit(10000)
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(self.mergeLists(l1, l2))
            lists = merged
        return lists[0]


    def mergeLists(self, l1, l2):
        out = ListNode(0)
        cur = out

        # base cases
        if not l1:
            cur.next = l2
            return out.next
        if not l2:
            cur.next = l1
            return out.next

        # recursive case
        if l1.val < l2.val:
            cur.next = ListNode(l1.val, self.mergeLists(l1.next, l2))
        else:
            cur.next = ListNode(l2.val, self.mergeLists(l1, l2.next))
        return out.next