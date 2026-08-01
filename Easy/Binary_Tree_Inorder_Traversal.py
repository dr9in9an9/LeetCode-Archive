# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        list = []
        if root.left != None:
            for each in self.inorderTraversal(root.left):
                list.append(each)
        list.append(root.val)
        if root.right != None:
            for each in self.inorderTraversal(root.right):
                list.append(each)

        return list
