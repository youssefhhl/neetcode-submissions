class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        p=[]
        for i in d:
            p+=[[i,d[i]]]
        p.sort(key=lambda x: x[1])
        r=[]
        for i in range(k):
            r.append(p[len(p)-1-i][0])
        return r