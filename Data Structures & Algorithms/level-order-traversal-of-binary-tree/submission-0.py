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

        trav = []
        nodes = deque()
        nodes.append(root)

        while nodes:
            children = []

            for _ in range(len(nodes)):
                curr = nodes.popleft()
                children.append(curr.val)

                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)


            trav.append(children)

        return trav