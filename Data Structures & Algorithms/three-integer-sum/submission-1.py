class Solution:

    def twoSum(self, numbers: List[int], target: int):
        numbers.sort()
        n=len(numbers)
        i=0
        j=n-1
        L=[]
        while i<j :
            x=numbers[i]+numbers[j]
            if x>target:
                j-=1
            elif x<target:
                i+=1
            else:
                L.append([-target,numbers[i],numbers[j]])
                i+=1
        print(L)
        return L

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        output=[]
        for i in range(n):
            numbers=nums.copy()
            numbers.pop(i)
            target=-nums[i]
            L=self.twoSum(numbers,target)
            if L:
                for l in L:
                    l.sort()
                    if l not in output:
                        output.append(l)
        return output        