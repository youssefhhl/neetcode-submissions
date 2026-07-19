class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=n-1
        r=nums[0]
        while i<=j:
            m=(i+j)//2
            if nums[m]<nums[j]:
                j=m-1
            else:
                i=m+1
            r=min(nums[m],r)
        return r