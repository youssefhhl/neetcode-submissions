class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        j=n-1
        s=(j-i)*min(heights[j],heights[i])
        while i<j:
            s2=(j-i)*min(heights[j],heights[i])
            s=max(s2,s)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return s