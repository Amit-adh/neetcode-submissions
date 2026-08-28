# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
 
        def serialize(node):
            res = []

            def preorder(node):
                if not node:
                    res.append("#")
                    return

                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

            preorder(node)

            return "".join(res)

        root_string = serialize(root)
        sub_string = serialize(subRoot)

        lps = [0] * len(sub_string)

        # build lps
        j = 0
        
        for i in range(1, len(sub_string)):
            while j > 0 and sub_string[i] != sub_string[j]:
                j = lps[j-1]

            if sub_string[i] == sub_string[j]:
                j += 1

            lps[i] = j

        #KMP
        j = 0

        for i in range(len(root_string)):
            while j > 0 and root_string[i] != sub_string[j]:
                j = lps[j-1]

            if sub_string[j] == root_string[i]:
                j += 1

            if j == len(sub_string):
                return True
        
        return False