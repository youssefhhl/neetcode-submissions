class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        for i in range(n):
            dic[nums[i]]=i
        s=0
        for x in nums:
            if x-1 not in dic:
                i=1
                while x+i in dic:
                    i+=1
                s=max(s,i)
        return s