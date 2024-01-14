class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        v1, v2 = [], []
        n, m = len(word1), len(word2)
        mp1, mp2 = defaultdict(int), defaultdict(int)

        if n != m:
            return False

        for i in range(n):
            mp1[word1[i]] += 1
            mp2[word2[i]] += 1

        for x in mp1:
            v1.append(mp1[x])
            if x not in mp2:
                return False

        for x in mp2:
            v2.append(mp2[x])
            if x not in mp1:
                return False

        if len(v1) != len(v2):
            return False

        n = len(v1)
        v1.sort()
        v2.sort()

        for i in range(n):
            if v1[i] != v2[i]:
                return False

        return True