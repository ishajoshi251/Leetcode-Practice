class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        ans =  1
        maxi = pairs[-1][0]
        for i in range(len(pairs)-1,-1,-1):
            if maxi> pairs[i][1]:
                maxi = pairs[i][0]
                ans += 1
                
            
        return ans
               