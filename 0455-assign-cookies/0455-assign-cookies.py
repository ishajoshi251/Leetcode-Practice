class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        j = 0
        
        for i in range(len(s)):
            if j<len(g) and g[j]<=s[i]:
                count += 1
                j += 1
            else:
                continue
        return count