# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invTree(root):
            # base cases
            if not root:
                return None
            # recursive case
            tmp = root.left
            root.left = root.right
            root.right = tmp
            invTree(root.left)
            invTree(root.right)
        invTree(root)
        return root