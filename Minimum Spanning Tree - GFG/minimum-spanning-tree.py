#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        q = []
        vis = [0]*V
        heapq.heappush(q,[0,0])
        s = 0
        while q:
            wt,node = heapq.heappop(q)
            if vis[node] == 1:
                continue
            vis[node] = 1
            s += wt
            for i in adj[node]:
                v = i[0]
                w = i[1]
                
                if vis[v] == 0:
                    heapq.heappush(q,[w,v])
        return s
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends