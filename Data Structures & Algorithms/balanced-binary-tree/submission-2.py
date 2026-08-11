# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        out = True
        def dfs(root):
            nonlocal out

            if not root or not out:
                return 0
            left = dfs(root.left)
            if not out:
                return 0
            right = dfs(root.right)
            out = False if (abs(left - right) > 1) else out
            return 1 + max(left, right)
        dfs(root)
        return out
