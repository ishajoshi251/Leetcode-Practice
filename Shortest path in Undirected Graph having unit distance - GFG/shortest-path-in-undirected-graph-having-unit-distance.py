#User function Template for python3

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = [[] for i in range(n)]
        for i in range(m):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        dist = [float('inf')]*n
        dist[src] = 0
        q = []
        q.append(src)
        while q:
            node = q.pop(0)
            for i in adj[node]:
                if dist[i]>dist[node]+1:
                    dist[i] = dist[node]+1
                    q.append(i)
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

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends