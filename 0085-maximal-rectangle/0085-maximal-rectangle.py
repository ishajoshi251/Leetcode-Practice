class Solution(object):
    def largestRectangleArea(self, heights):
        
        n = len(heights)
        nsr = [0] * n
        nsl = [0] * n

        s = []

        for i in range(n - 1, -1, -1):
            while s and heights[i] <= heights[s[-1]]:
                s.pop()
            if not s:
                nsr[i] = n
            else:
                nsr[i] = s[-1]
            s.append(i)

        while s:
            s.pop()

        for i in range(n):
            while s and heights[i] <= heights[s[-1]]:
                s.pop()
            if not s:
                nsl[i] = -1
            else:
                nsl[i] = s[-1]
            s.append(i)

        ans = 0

        for i in range(n):
            ans = max(ans, heights[i] * (nsr[i] - nsl[i] - 1))
        return ans
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 0
        heights = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans,self.largestRectangleArea(heights))
        return ans