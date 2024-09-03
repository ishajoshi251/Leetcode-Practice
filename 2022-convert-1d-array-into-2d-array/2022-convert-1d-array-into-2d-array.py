class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = [[0 for j in range(n)]for i in range(m)]
        count = 0
        if n*m != len(original):
            return []
        for i in range(m):
            for j in range(n):
                ans[i][j] = original[count]
                count += 1
        return ans