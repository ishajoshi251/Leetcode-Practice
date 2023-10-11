class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0 for j in range(len(colSum))]for i in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                x = min(rowSum[i],colSum[j])
                ans[i][j] = x
                rowSum[i] -= x
                colSum[j] -= x
        return ans