class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p1=[1]*n
        p2=[1]*n
        r=[]
        for i in range(1,n):
            p1[i]=p1[i-1]*nums[i-1]
            p2[n-1-i]=p2[n-i]*nums[n-i]
        for i in range(n):
            r.append(p1[i]*p2[i])
        return r



