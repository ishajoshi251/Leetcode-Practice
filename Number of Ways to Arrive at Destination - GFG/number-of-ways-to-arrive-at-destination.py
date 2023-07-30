#User function Template for python3

from typing import List
from collections import defaultdict
import sys
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here
        mod = 10**9+7
        adj=[[] for i in range(n)]

        for u,v,w in roads:

            adj[u].append([v,w])

            adj[v].append([u,w])
        dist = [float('inf')]*n
        ways = [0]*n
        dist[0] = 0
        ways[0] = 1
        q = []
        heapq.heappush(q,[0,0])
        while q:
            node_dist, node = heapq.heappop(q)
            for neighbor, neighbor_dist in adj[node]:
                if node_dist + neighbor_dist < dist[neighbor]:
                    dist[neighbor] = node_dist + neighbor_dist
                    ways[neighbor] = ways[node]
                    heapq.heappush(q,[dist[neighbor], neighbor])
                elif node_dist + neighbor_dist == dist[neighbor]:
                    ways[neighbor] += (ways[node])%mod
        return ways[n-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        adj=[]
        
        for i in range(m):
            tmp =[]
            x,y,z=map(int,input().split())
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            adj.append(tmp)
            
        
        
        
       
        obj = Solution()
        res = obj.countPaths(n, adj)
        
        print(res)
        

# } Driver Code Ends