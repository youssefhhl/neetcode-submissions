class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        i=1
        j=piles[-1]
        k=piles[-1]
        while(i<=j):
            m=(i+j)//2
            x=0
            for p in piles:
                x+=p//m 
                if p%m!=0:
                    x+=1

            if x<=h:
                k=min(k,m)
                j=m-1
            else:
                i=m+1
        return k


