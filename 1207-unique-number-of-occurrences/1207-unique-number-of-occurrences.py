class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        s = []
        for i in d:
            s.append(d[i])
            
        if len(set(s)) == len(s):
            return True
        else:
            return False