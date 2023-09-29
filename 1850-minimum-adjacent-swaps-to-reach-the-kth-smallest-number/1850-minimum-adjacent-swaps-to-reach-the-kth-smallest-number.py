class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        
        x = num

        for _ in range(k):
            num = self.nextPermutation(num)

        ans = 0
        n = len(num)

        for i in range(n):
            if x[i] != num[i]:
                j = i + 1

                while num[i] != x[j]:
                    j += 1

                while j > i:
                    x = x[:j-1] + x[j] + x[j-1] + x[j+1:]
                    ans += 1
                    j -= 1

        return ans

    def nextPermutation(self,s):
        s = list(s)
        i = len(s) - 2

        while i >= 0 and s[i] >= s[i+1]:
            i -= 1

        if i >= 0:
            j = len(s) - 1
            while s[j] <= s[i]:
                j -= 1
            s[i], s[j] = s[j], s[i]

        s[i+1:] = reversed(s[i+1:])
        return ''.join(s)

