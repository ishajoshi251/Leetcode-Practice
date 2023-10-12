class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice= 0 
        bob = 0
        i = 0
        flag = True
        j = len(piles)-1
        while i<j:
            if flag:
                if piles[i]>piles[j]:
                    alice += piles[i]
                    i+=1
                else:
                    alice += piles[j]
                    j-=1
            else:
                if piles[i]>piles[j]:
                    bob += piles[i]
                    i+=1
                else:
                    bob += piles[j]
                    j-=1
        if alice>bob:
            return True
        else:
            return False