class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        p=0
        i=0
        j=1
        while(j<n):
            x=prices[j]-prices[i]
            if x>0:
                j+=1
                p=max(p,x)
            else:
                i=j
                j+=1
        return p
            