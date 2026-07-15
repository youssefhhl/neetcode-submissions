class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        n=len(numbers)
        for i in range(n):
            x=target-numbers[i]
            if x in dic:
                return [dic[x]+1,i+1]
            else:
                dic[numbers[i]]=i