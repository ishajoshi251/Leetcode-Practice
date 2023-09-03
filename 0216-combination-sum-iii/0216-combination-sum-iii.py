class Solution:
    def help(self,ans,candidates,n,k,temp,i):
        if i == len(candidates):
            if len(temp)==k and n == 0:
                ans.append(temp[:])
            return
        if candidates[i]<=n:
            temp.append(candidates[i])
            self.help(ans,candidates,n-candidates[i],k,temp,i+1)
            temp.pop()
        self.help(ans,candidates,n,k,temp,i+1)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = []
        for i in range(9):
            candidates.append(i+1)
        ans = []
        self.help(ans,candidates,n,k,[],0)
        return ans