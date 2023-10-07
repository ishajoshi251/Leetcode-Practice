
class Solution:
    def issub(self, s, pattern):
        i = 0
        j = 0
        while i < len(s) and j < len(pattern):
            if s[i] == pattern[j]:
                j += 1
            i += 1

        return j == len(pattern)

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        caps = 0
        for i in pattern:
            if 'A' <= i <= 'Z':
                caps += 1

        ans = []
        for s in queries:
            caps2 = 0
            for j in s:
                if 'A' <= j <= 'Z':
                    caps2 += 1
            if caps != caps2:
                ans.append(False)
            else:
                if self.issub(s, pattern):
                    ans.append(True)
                else:
                    ans.append(False)
        
        return ans
