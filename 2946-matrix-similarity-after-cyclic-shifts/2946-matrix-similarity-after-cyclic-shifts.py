class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        n = len(mat)
        m = len(mat[0])
        new = [row[:] for row in mat]
        k = k%m
        for i in range(n):
            if i%2 == 0:
                mat[i] = mat[i][::-1]
                mat[i][:m-k] = mat[i][:m-k][::-1]
                mat[i][m-k:] = mat[i][m-k:][::-1]
            else:
                mat[i] = mat[i][::-1]
                mat[i][:k] = mat[i][:k][::-1]
                mat[i][k:] = mat[i][k:][::-1]
        
        if mat == new:
            return True
        else:
            return False