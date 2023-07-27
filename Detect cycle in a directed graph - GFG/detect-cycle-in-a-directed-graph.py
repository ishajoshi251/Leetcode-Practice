#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        ind = [0]*V
        for i in range(V):
            for j in adj[i]:
                ind[j] += 1
        q = []
        topo = []
        for i in range(V):
            if ind[i] == 0:
                q.append(i)
        while q:
            node = q.pop(0)
            topo.append(node)
            for i in adj[node]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        if len(topo) == V:
            return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends