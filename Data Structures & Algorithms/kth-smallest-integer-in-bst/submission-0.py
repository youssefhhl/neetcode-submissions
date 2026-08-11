# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def bfs(root):
            if not root:
                return []
            else:
                L=[root.val]
                return bfs(root.left)+L+bfs(root.right)
        
        M=bfs(root)

        return M[k-1]