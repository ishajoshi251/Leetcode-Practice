class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum1 = 0
        
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j or i+j == len(mat) - 1:
                    sum1 += mat[i][j]
        
        
        return sum1 