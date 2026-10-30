class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        x=0
        while(i<j):
            s=(j-i)*min(heights[i],heights[j])
            x=max(s,x)
            if(heights[i]<heights[j]):
                i+=1
            else:
                j-=1
        return x
            