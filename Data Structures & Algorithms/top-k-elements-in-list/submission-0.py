class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            dic[i]=1+dic.get(i,0)
        L=list([dic[i],i] for i in dic)     
        L.sort(reverse=True)
        return [L[i][1] for i in range(k)]