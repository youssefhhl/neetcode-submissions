class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        m=1
        nums.sort()
        if n==0:
            return 0
        
        i=0
        while(i<n-1):
            if nums[i+1]-nums[i]==1:
                s=2
                i+=1
                while( i< n-1 and (nums[i+1]-nums[i]==1 or nums[i+1]-nums[i]==0) ):
                    if nums[i+1]-nums[i]==1:
                        i+=1
                        s+=1
                    else:
                        i+=1
                m=max(m,s)
            i+=1
        return m