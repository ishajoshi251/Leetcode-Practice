class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
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