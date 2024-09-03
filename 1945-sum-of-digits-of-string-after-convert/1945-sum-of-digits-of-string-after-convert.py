class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1 = ""
        sum = 0
        for i in range(len(s)):
            s1 += str(ord(s[i])-96)
        count = 0
        while count != k:
            for i in range(len(s1)):
                sum += int(s1[i])
            s1 = str(sum)
            sum = 0
            count += 1
        return int(s1)