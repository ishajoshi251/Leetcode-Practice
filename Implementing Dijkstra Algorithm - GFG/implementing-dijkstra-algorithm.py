import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist = [float('inf')]*V
        heap = []
        heapq.heappush(heap,[0,S])
        dist[S] = 0
        while heap:
            d,node = heapq.heappop(heap)
            for i in range(len(adj[node])):
                v = adj[node][i][0]
                w = adj[node][i][1]
                if d+w<dist[v]:
                    dist[v] = d+w
                    heapq.heappush(heap,[d+w,v])
                
        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends