class Solution:
    def help(self,ans,nums,n,i,temp):
        if i == n:
            ans.append(temp[:])
            return
        temp.append(nums[i])
        self.help(ans,nums,n,i+1,temp)
        temp.pop()
        self.help(ans,nums,n,i+1,temp)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.help(ans,nums,len(nums),0,[])
        return ans
   