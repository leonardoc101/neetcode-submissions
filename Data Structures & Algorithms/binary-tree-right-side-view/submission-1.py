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
        agenda.append(root)

        while agenda:
            level_len = len(agenda)
            first = True
            for i in range(level_len):
                node = agenda.popleft()
                if first:
                    out.append(node.val)
                    first = False
                for child in [node.right, node.left]:
                    if child:
                        agenda.append(child)
        return out