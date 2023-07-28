#User function Template for python3

from typing import List

class Solution:
    def toposort(self,node,vis,adj,stack):
        vis[node] = 1
        for i in range (len(adj[node])):
            v = adj[node][i][0]
            if vis[v] == 0:
                self.toposort(v,vis,adj,stack)
        stack.append(node)
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            w = edges[i][2]
            adj[u].append([v,w])
        vis = [0]*n
        stack = []
        for i in range(n):
            if vis[i] == 0:
                self.toposort(i,vis,adj,stack)
        dist = [float('inf')]*n
        dist[0] = 0
        while stack:
            node = stack.pop()
            for i in range(len(adj[node])):
                v = adj[node][i][0]
                w = adj[node][i][1]
                if dist[v]>dist[node]+w:
                    dist[v] = dist[node]+w
        ans = [-1]*n    
        for i in range(n):
            if dist[i] != float('inf'):
                ans[i] = dist[i]
            else:
                ans[i] = -1
            
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



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
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends