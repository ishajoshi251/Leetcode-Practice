#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q = []
        q.append(0)
        ans = []
        vis = [0]*V
        vis[0] = 1
        while q:
            node = q.pop(0)
            ans.append(node)
            for i in range(len(adj[node])):
                if not vis[adj[node][i]]:
                    q.append(adj[node][i])
                    vis[adj[node][i]] = 1
        return ans

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends