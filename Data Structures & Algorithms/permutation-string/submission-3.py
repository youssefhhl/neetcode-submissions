class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        d = {}
        window = {}

        for c in s1:
            d[c] = d.get(c, 0) + 1

        for i in range(n):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if d == window:
            return True

        left = 0

        for right in range(n, m):
            # Add the new character
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Remove the character leaving the window
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if d == window:
                return True

        return False