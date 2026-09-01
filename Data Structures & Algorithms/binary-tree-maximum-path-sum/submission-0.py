# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.curr_max = root.val

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            w_split = max(
                node.val,
                node.val + left,
                node.val + right
                )

            split = node.val + left + right

            self.curr_max = max(self.curr_max, split, w_split)

            return w_split

        dfs(root)

        return self.curr_max