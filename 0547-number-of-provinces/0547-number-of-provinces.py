class Solution:
    def dfs(self,node,vis,l):
        vis[node] = 1
        for i in l[node]:
            if not vis[i]:
                self.dfs(i,vis,l)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = [[] for i in range(1,len(isConnected)+1)]
        vis = [0]*(len(isConnected))
        count = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    l[i].append(j)
                    l[j].append(i)
        for i in range(len(l)):
            if not vis[i]:
                count += 1
                self.dfs(i,vis,l)
                
        return count