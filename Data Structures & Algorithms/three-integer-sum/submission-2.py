class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r=[]
        n=len(nums)
        for i in range(n-2):
            target=-nums[i]
            d=set()
            for j in range(i+1,n):
                x=target-nums[j]
                if x in d:
                    L=[nums[i],nums[j],x]
                    L.sort()
                    if L not in r:
                        r.append(L)
                    
                else:
                    d.add(nums[j])
        return r
