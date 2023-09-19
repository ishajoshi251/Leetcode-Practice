class Solution:
    def dfs(self,arr,i,vis):
       
        
        if i<0 or i>=len(arr) or vis[i] == 1:
            return False
        vis[i] = 1
        if arr[i] == 0:
            return True

        return self.dfs(arr,arr[i]+i,vis) or self.dfs(arr,i-arr[i],vis)
            
        
    def canReach(self, arr: List[int], start: int) -> bool:
        vis = [0]*len(arr)
        return self.dfs(arr,start,vis)