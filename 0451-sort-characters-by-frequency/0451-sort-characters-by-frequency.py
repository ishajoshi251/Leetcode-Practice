class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        d = {}
        for i in range(len(s)):
            if i not in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        ans = []
        ans = sorted(s,key=lambda x:(-d[x],x))
        return ' '.join(ans)
        '''
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ans = sorted(s, key=lambda x: (-d[x], x))
        return ''.join(ans)