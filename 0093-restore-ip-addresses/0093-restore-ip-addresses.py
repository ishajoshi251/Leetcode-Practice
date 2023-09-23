class Solution:
    def solve(self,i,temp,s,ans,k):
        if k>4:
            return
        if i == len(s):
            if k == 4:
                temp = temp[:-1]
                ans.append(temp)
                return
        for j in range(i,len(s)):
            curr = s[i:j+1]
            if (len(curr)>1 and curr[0] == '0') or int(curr)>255:
                break
            self.solve(j+1,temp+curr+'.',s,ans,k+1)
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
       
        self.solve(0,"",s,ans,0)
        return ans