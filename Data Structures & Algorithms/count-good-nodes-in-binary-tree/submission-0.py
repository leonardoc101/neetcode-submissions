# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good = 0
        def dfs_helper(node, largest_previous):
            nonlocal good

            if not node:
                return None
            if node.val >= largest_previous:
                good += 1
                largest_previous = node.val
            dfs_helper(node.left, largest_previous)
            dfs_helper(node.right, largest_previous)
        dfs_helper(root, float("-inf"))
        return good
        