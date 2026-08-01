# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        if root != None:
            for subtree in [self.postorderTraversal(root.left), self.postorderTraversal(root.right)]:
                for eachVal in subtree:
                    ls.append(eachVal)
            ls.append(root.val)
        return ls
