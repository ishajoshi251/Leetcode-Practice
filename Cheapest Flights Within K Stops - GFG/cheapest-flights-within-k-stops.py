#User function Template for python3
from typing import List
class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        adj = [[] for i in range(n)]
        q = []
        for i in range(len(flights)):
            adj[flights[i][0]].append([flights[i][1],flights[i][2]])
        q.append([0,src,0])
        dist = [float('inf')]*n
        dist[src] = 0
        while q:
            steps,node,cost = q.pop(0)
            if steps>k:
                continue
            for i in range(len(adj[node])):
                adjnode = adj[node][i][0]
                ew = adj[node][i][1]
                if cost+ew<dist[adjnode] and steps<=k:
                    dist[adjnode] = cost+ew
                    q.append([steps+1,adjnode,cost+ew])
                
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,edge=map(int,input().split())
        flights=[]
        for _ in range(edge):
            temp=list(map(int,input().split()))
            flights.append(temp[:])
        src=int(input())
        dst=int(input())
        k=int(input())
        obj=Solution()
        res=obj.CheapestFLight(n,flights,src,dst,k)
        print(res)

        
        
# } Driver Code Ends