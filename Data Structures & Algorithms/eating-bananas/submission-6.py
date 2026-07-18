class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        i=1
        j=max(piles)
        m=(i+j)//2
        k=j
        while i<=j:
            s=0
            m=(i+j)//2
            for l in range(n):
                if piles[l]%m==0:
                    s+=piles[l]//m
                else:
                    s+=piles[l]//m+1
            if s>h:
                i=m+1
            else:
                j=m-1
                k=m

        return k
        