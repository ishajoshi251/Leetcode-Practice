class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for i in range(n+1)]
        for i in times:
            source, dest, travelTime = i
            adj[source].append((travelTime, dest))
        
        dist = [float('inf')] *(n+1)
        dist[k] = 0
        q = []
        q.append(k)
        while q:
                currNode = q.pop(0)
                
                for time, adjnode in adj[currNode]:
                    arrivalTime = dist[currNode] + time
                    if dist[adjnode] > arrivalTime:
                        
                        dist[adjnode] = arrivalTime
                        q.append(adjnode)
        
        for i in range(1,n+1):
            if dist[i] == float('inf'):
                return -1
        return max(dist[1:])


