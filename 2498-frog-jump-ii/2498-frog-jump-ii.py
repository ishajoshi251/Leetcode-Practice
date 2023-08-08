class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return (stones[-1] - stones[0])
    
        maxjump = 0
        for i in range(len(stones)-2):
            jump = stones[i+2] - stones[i]
            maxjump = max(maxjump, jump)
            
        return maxjump
