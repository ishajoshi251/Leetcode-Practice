class Solution:
    def minDeletions(self, s: str) -> int:
        d1 = {}
        d2 = {}
        count = 0
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in d1:
            a = d1[i]
            if a not in d2:
                d2[a] = i
            else:
                while a in d2:
                    a -= 1
                    count += 1
                    if a == 0:
                        break
                d2[a] = i
        return count
                