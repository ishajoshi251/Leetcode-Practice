class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        while hand:
            start = hand[0]
            for i in range(groupSize):
                if start+i not in hand:
                    return False
                else:
                    hand.remove(start+i)
                   
        return True
