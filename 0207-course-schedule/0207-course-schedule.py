class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        adj = [[] for i in range(num)]
        for i in range(len(pre)):
            adj[pre[i][0]].append(pre[i][1])
        ind = [0]*num
        for i in range(num):
            for j in adj[i]:
                ind[j] += 1
        topo = []
        q = []
        for i in range(len(ind)):
            if ind[i] == 0:
                q.append(i)
        
        while q:
            node = q.pop(0)
            topo.append(node)
            for i in adj[node]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        if len(topo) == num:
            return True
        return False