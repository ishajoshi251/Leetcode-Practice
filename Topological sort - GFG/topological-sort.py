class Solution:
    
    #Function to return list containing vertices in Topological order.
    def dfs(self,node,vis,V,adj,stack):
        vis[node] = 1
        for i in adj[node]:
            if vis[i] == 0:
                self.dfs(i,vis,V,adj,stack)
        stack.append(node)
    def topoSort(self, V, adj):
        # Code here\
        stack = []
        ans = []
        vis = [0]*V
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i,vis,V,adj,stack)
        while stack:
            ans.append(stack.pop())
        return ans

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends