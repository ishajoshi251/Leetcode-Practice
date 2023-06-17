class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        while num>0:
            s += num%10
            num = num//10
            if num == 0 and s > 9:
                num = s
                s = 0
        return s