class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        L=[[position[i],speed[i]] for i in range(n)]
        L.sort()
        R=[(target-L[i][0])/L[i][1] for i in range(n)]
        stack=[]
        for i in R:
            while stack and i>=stack[-1]:
                stack.pop()
            stack.append(i)
        return len(stack) 