# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "None"

        treeList = [str(root.val) + "*"]
        agenda = deque()
        agenda.append(root)

        while agenda:
            node = agenda.popleft()
            for child in [node.left, node.right]:
                if child:
                    treeList.append(str(child.val) + "*")
                    agenda.append(child)
                else:
                    treeList.append("None*")
        treeString = "".join(treeList)
        print(treeString)
        return treeString

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split("*")
        if vals[0] == "None":
            return None
        root = TreeNode(int(vals[0]))
        agenda = deque([root])
        idx = 1
        while agenda:
            node = agenda.popleft()
            if vals[idx] != "None":
                node.left = TreeNode(int(vals[idx]))
                agenda.append(node.left)
            idx += 1
            if vals[idx] != "None":
                node.right = TreeNode(int(vals[idx]))
                agenda.append(node.right)
            idx += 1
        return root
