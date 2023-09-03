class Solution:
    def help(self,ans,temp,n,open,close):
        if 2*n == len(temp):
            ans.append(temp)
            return
        if open<n:
            temp += '('
            self.help(ans,temp,n,open+1,close)
            temp = temp[:-1]
        if close<open:  
            temp += ')'
            self.help(ans,temp,n,open,close+1)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.help(ans,'',n,0,0)
        return ans
        