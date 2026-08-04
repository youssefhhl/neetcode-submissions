# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        queue=[root]
        while queue:
            l=len(queue)
            level=[]
            for i in range(l):
                n=queue.pop(0)
                if n:
                    level.append(n.val)
                    queue.append(n.left)
                    queue.append(n.right)
                
            if level:
                output.append(level[-1])
        return output