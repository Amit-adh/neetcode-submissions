# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preorder(n1, n2):
            if not n1 and not n2:
                return True

            elif (n1 and not n2) or (n2 and not n1):
                return False

            if n1.val != n2.val:
                return False

            
            left = preorder(n1.left, n2.left)
            right = preorder(n1.right, n2.right)

            return left and right

        nodes = deque()
        nodes.append(root)

        while nodes:
            curr = nodes.pop()

            if not curr:
                continue

            if preorder(curr, subRoot):
                return True

            nodes.append(curr.left)
            nodes.append(curr.right)

        return False