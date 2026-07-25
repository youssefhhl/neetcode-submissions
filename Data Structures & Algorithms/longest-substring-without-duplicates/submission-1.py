class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        n=len(s)
        l=0
        r=0
        i=0
        while i<n:
            if s[i] not in dic:
                l+=1
                dic[s[i]]=i
                i+=1
            else:
                i=dic[s[i]]+1
                print(l,"  ",r)
                r=max(r,l)
                l=0
                dic={}
        return max(r,l)

