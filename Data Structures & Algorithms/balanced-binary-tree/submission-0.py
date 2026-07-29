# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif abs(self.hight(root.right)-self.hight(root.left))>1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)





    def hight(self,root):
        if not root:
            return 0
        else:
            return max(self.hight(root.left),self.hight(root.right)) +1