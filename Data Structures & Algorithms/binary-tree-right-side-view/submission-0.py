# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        out = []
        agenda = deque()
        agenda.append((0, root))

        while agenda:
            idx, node = agenda.popleft()
            if idx >= len(out):
                out.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    agenda.append((idx + 1, child))
        return out