class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        left = 0
        d = {}
        for right in range(len(s)):
            if s[right] in d:
                d[s[right]] += 1
            else:
                d[s[right]] = 1
           
            while (right-left+1)- max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
                
            res = max(right-left+1,res)
        return res
            