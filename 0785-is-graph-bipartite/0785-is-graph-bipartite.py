class Solution:
    def dfs(self,color,col,graph,node):
        color[node] = col
        for i in graph[node]:
            if color[i] == -1:
                if self.dfs(color,not col,graph,i) == False:
                    return False
            elif color[i] == col:
                return False
        return True
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        for i in range(len(graph)):
            if color[i] == -1:
                if self.dfs(color,0,graph,i) == False:
                    return False
        
        return True   
	
        