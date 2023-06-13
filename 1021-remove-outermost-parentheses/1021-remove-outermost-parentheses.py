class Solution:
    def removeOuterParentheses(self, s: str) -> str:
       
        
        count = 1
        temp = ""
        ans = ""
        i = 1
        while i<len(s):
            
            if s[i] == '(':
                count += 1
                temp += s[i]
            else:
                count -= 1
                if count != 0:
                    temp += s[i]
            
            if count == 0:
                ans += temp
                temp = ""
                i += 1
                count = 1
            i += 1
                
                
                 
                
        return ans