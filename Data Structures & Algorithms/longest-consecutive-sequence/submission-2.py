class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic=set(nums)
        n=len(nums)
        s=0
        for x in nums:
            if x-1 not in dic:
                i=1
                while x+i in dic:
                    i+=1
                s=max(s,i)
        return s