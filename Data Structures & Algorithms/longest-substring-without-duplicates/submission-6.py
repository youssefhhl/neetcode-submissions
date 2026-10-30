class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        left = 0
        r = 0
        d = {}

        while j < len(s):
            if s[j] in d:
                left = max(left, d[s[j]] + 1)

            d[s[j]] = j
            r = max(r, j - left + 1)
            j += 1

        return r


            

