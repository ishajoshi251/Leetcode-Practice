#User function Template for python3
import heapq
class Solution:
        
    def MinimumEffort(self, a):
        #code here
        
        n = len(a)
        m = len(a[0])  # Corrected: Use len(a[0]) directly
        dist = [[float('inf') for j in range(m)] for i in range(n)]
        dist[0][0] = 0
        q = []
        heapq.heappush(q, [dist[0][0], 0, 0])
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        while q:
            d, r, c = heapq.heappop(q)
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr >= 0 and nc >= 0 and nr < n and nc < m:
                    new = max(abs(a[r][c] - a[nr][nc]), d)
                    if new < dist[nr][nc]:
                        dist[nr][nc] = new
                        heapq.heappush(q, [new, nr, nc])
        return dist[n - 1][m - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends