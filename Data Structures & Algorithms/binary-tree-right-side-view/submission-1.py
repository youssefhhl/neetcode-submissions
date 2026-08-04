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

            rightside=None
            l=len(queue)
            for i in range(l):
                n=queue.pop(0)
                if n:
                    rightside=n
                    queue.append(n.left)
                    queue.append(n.right)
                
            if rightside:
                output.append(rightside.val)
        return output