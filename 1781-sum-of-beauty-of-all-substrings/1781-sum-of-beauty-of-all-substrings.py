class Solution:
    def beautySum(self, s: str) -> int:
        '''
        beauty = 0
        for i in range(len(s)-2):
            d = {}
            for j in range(i,len(s)):
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
                beauty += (max(d.values()) - min(d.values()))
            d.clear()
        return beauty
        '''
        ans = 0 
        for i in range(len(s)):
            freq = [0]*26
            for j in range(i, len(s)):
                freq[ord(s[j])-97] += 1
                mini = 100000000000
                maxi = -11111111111
                for i in freq:
                    if i != 0:
                        mini = min(mini,i)
                        maxi = max(maxi,i)
                ans += maxi-mini
            
        return ans 
                