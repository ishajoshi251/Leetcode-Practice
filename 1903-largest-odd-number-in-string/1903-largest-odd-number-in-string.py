class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 != 0:
                num = num[:i+1]
                return num
        return ""