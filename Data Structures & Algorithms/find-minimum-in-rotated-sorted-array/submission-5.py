class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=n-1
        k=nums[0]
        while(i<=j):
            m=(i+j)//2
            k=min(k,nums[m])
            if(nums[m]>=nums[i]):
                if nums[m]<nums[j]:
                    j=m-1
                else:
                    i=m+1
            else:
                j=m-1
        return k
                