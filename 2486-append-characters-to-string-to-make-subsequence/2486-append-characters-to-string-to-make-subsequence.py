class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        count = len(t)
        i = j = 0
        while i<n and j<m:
            if s[i] == t[j]:
                count -= 1
                i += 1
                j += 1
            else:
                i += 1
        return count