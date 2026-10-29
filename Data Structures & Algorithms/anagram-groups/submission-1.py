class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=[]
        d={}
        n=len(strs)
        for s in strs:
            s1 = ''.join(sorted(s))
            if s1 not in d:
                d[s1]=[s]
            else:
                d[s1]+=[s]
        for s in d:
            r.append(d[s])
        return r

