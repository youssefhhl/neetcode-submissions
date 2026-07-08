class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dic={}
        for i in range(n):
            x=target-nums[i]
            if x in dic :
                return [dic[x],i]
            else :
                dic[nums[i]]=i

