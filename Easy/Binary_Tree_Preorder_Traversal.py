# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root != None:
            ls = [root.val]
            lf = self.preorderTraversal(root.left)
            if lf != []:
                for each in lf:
                    ls.append(each)
            rh = self.preorderTraversal(root.right)
            if rh != []:
                for each in rh:
                    ls.append(each)
            return ls
        return []
