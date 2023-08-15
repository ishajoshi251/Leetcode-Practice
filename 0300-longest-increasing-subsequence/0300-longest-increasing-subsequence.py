class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        dp[0]=1
        for i in range(1,len(nums)):
            maxi=0
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    maxi=max(maxi,dp[j])
            dp[i]=1+maxi
            
        return max(dp)