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
            return ""

        string = ""

        nodes = deque()
        nodes.append(root)

        res = []

        while nodes:
            curr = nodes.popleft()

            if not curr:
                res.append("#")
                continue
            
            res.append(str(curr.val))

            if curr:
                nodes.append(curr.left)
                nodes.append(curr.right)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or len(data) == 0:
            return None

        vals = data.split(",")

        root = TreeNode(int(vals[0]))
        nodes = deque()
        nodes.append(root)
        i = 1

        while nodes:
            curr = nodes.popleft()

            if not curr:
                continue

            if i < len(vals) and vals[i] == "#":
                curr.left = None
            else:
                curr.left = TreeNode(int(vals[i]))

            i += 1
                
            if i < len(vals) and vals[i] == "#":
                curr.right = None
            else:
                curr.right = TreeNode(int(vals[i]))

            i += 1

            nodes.append(curr.left)
            nodes.append(curr.right)


        return root






