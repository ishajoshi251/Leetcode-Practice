class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxi = 0
        for i in s:
            if i =='(':
                count += 1
            elif i == ')':
                count -= 1
            maxi = max(count,maxi)
        return maxi