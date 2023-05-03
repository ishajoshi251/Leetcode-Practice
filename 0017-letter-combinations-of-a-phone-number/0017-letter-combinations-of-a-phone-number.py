class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        a = []
        for i in range(len(digits)):
            a.append(int(digits[i]))
        d={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        ans = []
        s = ''
        self.helper(0,s,a,d,ans)
        return ans
    def helper(self,i,s,a,d,ans):
        if len(s) == len(a):
            ans.append(s)
            return
        curr = d[a[i]]
        for j in range(len(curr)):
            s += curr[j]
            self.helper(i+1,s,a,d,ans)
            s = s[:-1]
        