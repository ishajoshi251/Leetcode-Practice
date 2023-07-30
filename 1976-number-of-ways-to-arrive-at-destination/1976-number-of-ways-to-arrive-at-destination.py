class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
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
        return ways[n-1]%mod