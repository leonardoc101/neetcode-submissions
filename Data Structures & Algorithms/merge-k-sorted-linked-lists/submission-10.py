# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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

        while l1 or l2:
            if not l1:
                cur.next = ListNode(l2.val, l2.next)
                break
            if not l2:
                cur.next = ListNode(l1.val, l1.next)
                break
            if l1.val < l2.val:
                cur.next = ListNode(l1.val, None)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val, None)
                l2 = l2.next
            cur = cur.next
        return out.next
