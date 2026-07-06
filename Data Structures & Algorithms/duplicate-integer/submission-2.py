class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        n=len(nums)
        for i in range(n):
            dic[nums[i]]=i
        return not len(dic)==n
        