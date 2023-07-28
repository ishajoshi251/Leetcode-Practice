import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        


    # Create a DIST ARRAY and mark as dist infinite
        dist = [float('inf')] * V
    
        # Priority queue (min heap) to store nodes with their distances
        pq = []
    
        # Source node dist is zero
        dist[S] = 0
    
        # Push source node with dist into the priority queue
        heapq.heappush(pq, (0, S))
    
        while pq:
            dis, node = heapq.heappop(pq)
    
            # Explore the neighbors of the current node
            for it in adj[node]:
                adjNode, adjWeight = it[0], it[1]
    
                # If a shorter path is found, update the distance and add it to the priority queue
                if dis + adjWeight < dist[adjNode]:
                    dist[adjNode] = dis + adjWeight
                    heapq.heappush(pq, (dist[adjNode], adjNode))
    
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