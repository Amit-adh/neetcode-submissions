# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
 
        def serialize(root):

            res = []

            def preorder(node):
                if not node:
                    res.append("#")
                    return

                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)


            preorder(root)

            return res


        rootString = serialize(root)
        subString = serialize(subRoot)

        # build LPS
        lps = [0] * len(subString)
        j = 0

        for i in range(1, len(subString)):
            if j > 0 and subString[j] != subString[i]:
                j = lps[j - 1]

            if subString[j] == subString[i]:
                j += 1

            lps[i] = j
        

        # KMP
        j = 0
        for i in range(len(rootString)):
            while j > 0 and subString[j] != rootString[i]:
                j = lps[j - 1]

            if subString[j] == rootString[i]:
                j += 1

            if j == len(subString):
                return True

        return False