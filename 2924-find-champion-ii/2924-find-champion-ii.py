class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = [[i] for i in range(n)]
        ind = [0]*n
        ans = -1
        count =0
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            ind[edges[i][1]] += 1
        
        for i in range(n):
            if ind[i] == 0:
                count += 1
                ans = i
                if count>1:
                    return -1
        
        return ans