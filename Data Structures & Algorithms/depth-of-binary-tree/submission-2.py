# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        i = 1
        agenda = [(i, root)]
        visited = {root}

        while agenda:
            i, node = agenda.pop(0)
            if node is None:
                continue
            for n in {node.left, node.right}:
                if n not in visited and n is not None:
                    agenda.append((i + 1, n))
                    visited.add(n)
        return i
