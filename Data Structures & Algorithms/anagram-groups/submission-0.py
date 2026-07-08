class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        L=[sorted(s) for s in strs]
        dic={}
        for i in range(n):
            if "".join(L[i]) in dic:
                dic["".join(L[i])]+=[i]
            else:
                dic["".join(L[i])]=[i]
        return [[strs[i] for i in dic[j]] for j in dic ]
        
        
