# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        agenda = [(0, root)]
        out = []
        while agenda:
            idx, node = agenda.pop(0)
            if idx > len(out) - 1:
                out.append([node.val])
            else:
                out[idx].append(node.val)
            for child in [node.left, node.right]:
                if not child:
                    continue
                agenda.append((idx + 1, child))
        return out
