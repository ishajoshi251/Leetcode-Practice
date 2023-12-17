class Solution:
    def getGoodIndices(self, v: List[List[int]], t: int) -> List[int]:
        ans = []
        for i in range(len(v)):
            a = v[i][0]
            b = v[i][1]
            c = v[i][2]
            m = v[i][3]
            if (((a**b)%10)**c)%m == t:
                ans.append(i)
            
        return ans