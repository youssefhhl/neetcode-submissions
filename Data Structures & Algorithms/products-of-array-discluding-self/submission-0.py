class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        g=[1]*n
        l=[1]*n
        for i in range(1,n):
            g[i]=g[i-1]*nums[i-1]
            l[n-i-1]=l[n-i]*nums[n-i]
        output=[1]*n
        for i in range(n):
            output[i]=g[i]*l[i]

        return output    