#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self,V,adj,ans,vis,start):
            vis[start] = 1
            ans.append(start)
            
            for i in adj[start]:
                if not vis[i]:
                    self.dfs(V,adj,ans,vis,i)
    def dfsOfGraph(self, V, adj):
        # code here
        
        vis = [0]*V
       
        ans = []
        for i in range(V):
            if not vis[i]:
                self.dfs(V,adj,ans,vis,i)
        return ans
    
       
#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends