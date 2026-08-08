# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        if not head.next:
            return None

        slow, fast = head, head.next
        for _ in range(n):
            if fast is None:
                return head.next
            fast = fast.next
            
        while fast is not None:
            slow = slow.next
            fast = fast.next
        # slow = node before removed
        nxt = slow.next.next
        slow.next = nxt
        return head
        