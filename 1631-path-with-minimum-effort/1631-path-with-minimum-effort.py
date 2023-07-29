import heapq
class Solution:
    def minimumEffortPath(self, a: List[List[int]]) -> int:
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