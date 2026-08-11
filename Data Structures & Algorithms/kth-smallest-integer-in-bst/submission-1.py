# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(root):
            if not root:
                return []
            else:
                L=[root.val]
                return dfs(root.left)+L+dfs(root.right)
        
        M=dfs(root)

        return M[k-1]