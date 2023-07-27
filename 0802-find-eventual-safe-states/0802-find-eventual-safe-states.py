class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = [[] for i in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                adj[j].append(i)
        ind = [0]*len(graph)
        for i in range(len(graph)):
            for j in adj[i]:
                ind[j] += 1
        q = []
        for i in range(len(graph)):
            if ind[i] == 0:
                q.append(i)
        topo = []
        while q:
            node =q.pop(0)
            topo.append(node)
            for i in adj[node]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        return sorted(topo)
            