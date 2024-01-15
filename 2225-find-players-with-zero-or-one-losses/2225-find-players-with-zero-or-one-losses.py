class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = []
        los = []
        ans = []
        n = len(matches)
        d = {}
        for i in range(n):
            if matches[i][1] in d:
                d[matches[i][1]] += 1
            else:
                d[matches[i][1]] = 1
        for i in range(n):
            if matches[i][0] not in d.keys() and matches[i][0] not in win:
                win.append(matches[i][0])
        for i in d:
            if d[i] == 1:
                los.append(i)
        win.sort()
        los.sort()
        ans.append(win)
        ans.append(los)
        return ans