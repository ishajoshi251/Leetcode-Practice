class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        
        # Calculate the total product of all elements in grid
        total_product = 1
        left = [[1 for j in range(m)]for i in range(n)]
        right = [[1 for j in range(m)]for i in range(n)]
        
        
        for i in range(n):
            for j in range(m):
                left[i][j] = total_product
                total_product = (total_product * grid[i][j]) % 12345
                
        total_product = 1   
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                right[i][j] = total_product
                total_product = (total_product * grid[i][j]) % 12345
                
        result = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                # Calculate result using the total product and modulo
                result[i][j] = (left[i][j]*right[i][j]) % 12345
        
        return result