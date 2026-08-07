# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ls = []
        if root != None:
            ls.append(root.val)
            if root.left != None:
                ls.append(root.left.val)
                self._search(root.left, ls)
            if root.right != None:
                ls.append(root.right.val)
                self._search(root.right, ls)
                
        for i in range(0, len(ls)):
            num1 = ls[i]
            check = ls[0:i]
            if i + 1 < len(ls):
                check = check + ls[i+1:len(ls)]
            print(ls)
            for num2 in check:
                if (num1 + num2 == k):
                    return True
        
        return False

    def _search(self, root: Optional[TreeNode], ls):
        if root.left != None:
            ls.append(root.left.val)
            self._search(root.left, ls)
        if root.right != None:
            ls.append(root.right.val)
            self._search(root.right, ls)
