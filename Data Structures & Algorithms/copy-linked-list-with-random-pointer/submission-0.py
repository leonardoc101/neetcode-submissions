"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        original_nodes = {}
        random_pointers = {}
        cur, deepCopy = head, Node(0, None, None)
        deepCopyHead = deepCopy

        i = 0
        # assign original nodes to indices
        while cur is not None:
            original_nodes[cur] = i
            i += 1
            cur = cur.next
        i = 0
        cur = head

        # assign random pointer indices
        while cur is not None:
            if cur.random is not None:
                random_pointers[i] = original_nodes[cur.random]
            else:
                random_pointers[i] = -1
            i += 1
            cur = cur.next
        i = 0
        cur = head

        # make deepCopy with no random pointers
        while cur is not None:
            deepCopy.next = Node(cur.val, None, None)
            deepCopy = deepCopy.next
            nodes[i] = deepCopy
            i += 1
            cur = cur.next
        i = 0
        cur = deepCopyHead.next

        # assign random pointers
        while cur is not None:
            if random_pointers[i] != -1:
                cur.random = nodes[random_pointers[i]]
            else:
                cur.random = None
            i += 1
            cur = cur.next

        return deepCopyHead.next