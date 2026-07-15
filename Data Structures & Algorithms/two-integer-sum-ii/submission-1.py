class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        while i<j and numbers[i]+numbers[j]!=target:
            x=numbers[i]+numbers[j]
            if x>target:
                j-=1
            else:
                i+=1
        return [i+1,j+1]