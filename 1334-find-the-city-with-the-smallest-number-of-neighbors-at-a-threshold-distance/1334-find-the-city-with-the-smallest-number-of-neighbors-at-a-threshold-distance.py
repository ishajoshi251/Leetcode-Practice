class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[1e9]*n for _ in range(n)]
        for i in edges: 
            dist[i[0]][i[1]] = i[2]
            dist[i[1]][i[0]] = i[2]
        for i in range(0,n):
             dist[i][i]=0

        for k in range(0,n):
            for i in range(0,n):
                for j in range(0,n):
                    if dist[i][k]==1e9 or dist[k][j]==1e9: continue
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

        cityNo,cntCity=-1,n
        for city in range(0,n):
            cnt = 0
            for adjC in range(0,n):
                if dist[city][adjC]<=distanceThreshold:
                    cnt+=1
            if cnt<=cntCity:
                cntCity=cnt
                cityNo=city
        return cityNo