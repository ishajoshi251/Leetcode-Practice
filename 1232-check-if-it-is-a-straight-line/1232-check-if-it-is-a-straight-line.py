class Solution(object):
    def checkStraightLine(self, c):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x0 = c[0][0]
        y0 = c[0][1]
        dx = c[1][0]-x0
        dy = c[1][1]-y0
        for i in range(len(c)):
            x = c[i][0]
            y = c[i][1]
            if dx*(y-y0) != dy*(x-x0):
                return False
        return True
        