class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        m=(i+j)//2
        while i<j and nums[m]!=target:
            if nums[m]>target:
                j=m-1
            else:
                i=m+1
            m=(i+j)//2

        if nums[m]==target:
            return m
        return -1