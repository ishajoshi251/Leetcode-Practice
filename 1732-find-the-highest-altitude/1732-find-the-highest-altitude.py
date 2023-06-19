class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l = []
        l.append(0)
        sum1 = 0
        for i in gain:
            sum1 = sum1 + i
            l.append(sum1)
        return max(l)
            