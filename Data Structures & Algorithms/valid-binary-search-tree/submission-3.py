# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        agenda = deque()
        agenda.append((float("-inf"), float("inf"), root))

        while agenda:
            low, high, node = agenda.popleft()
            if not (low < node.val < high):
                return False
            left, right = node.left, node.right
            if left:
                agenda.append((low, node.val, left))
            if right:
                agenda.append((node.val, high, right))
        return True