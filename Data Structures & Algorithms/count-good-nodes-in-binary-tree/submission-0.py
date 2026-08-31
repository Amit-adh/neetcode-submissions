# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.good = 0

        def preorder(node, curr_max):
            if not node:
                return

            if node.val >= curr_max:
                self.good += 1

            curr_max = max(node.val, curr_max)

            preorder(node.left, curr_max)
            preorder(node.right, curr_max)

        preorder(root, root.val)

        return self.good