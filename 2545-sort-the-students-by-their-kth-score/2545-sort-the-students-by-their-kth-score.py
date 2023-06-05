class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        ans = []
        for i in range(len(score)):
            ans.append([score[i][k],score[i]])
        ans = sorted(ans, key=lambda x: -x[0])
        for i in range(len(score)):
            score[i] = ans[i][1]
        return score
            
        