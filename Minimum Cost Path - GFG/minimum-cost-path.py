import heapq
class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
		#Code here
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf') for j in range(m)]for i in range(n)]
        dp[0][0] = grid[0][0]
        q = []
        heapq.heappush(q,[dp[0][0],0,0])
        dr = [0,0,1,-1]
        dc =[1,-1,0,0]
        while q:
            d,i,j = heapq.heappop(q)
            if i == n-1 and j == m-1:
                return d
            for k in range(4):
                nr = i+dr[k]
                nc = j+dc[k]
                if nr>=0 and nr<n and nc>=0 and nc<m and dp[nr][nc]>grid[nr][nc]+d:
                    dp[nr][nc] = grid[nr][nc]+d
                    heapq.heappush(q,[dp[nr][nc],nr,nc])
             
        return -1
            

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends