class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if 48<=ord(s[0])<=57:
                return int(s)
            else:
                return 0
        
        sign = 1
        if (s[0] == '-' and s[1] == ' ') or (s[0] == '-' and s[1] == ' '):
            return 0
        
        else:
            j = 0
            while j<len(s):
                if s[j] == ' ':
                    j += 1
                else:
                    break
            if j >= len(s):
                return 0
            if s[j] == '-':
                sign = -1
                for i in range(j+1,len(s)):
                    if 48<=ord(s[i])<=57:
                        ans += s[i]
                    elif s[i] == ' ':
                        break
                    else:
                        break
            elif s[j] == '+':  
                for i in range(j+1,len(s)):
                    if 48<=ord(s[i])<=57:
                        ans += s[i]
                    elif s[i] == ' ':
                        break
                    else:
                        break
            else:
                for i in range(j,len(s)):
                    if 48<=ord(s[i])<=57:
                        ans += s[i]
                    elif s[i] == ' ':
                        break
                    else:
                        break
        if len(ans) == 0:
            return 0
        if (sign*int(ans)<0) and (sign*int(ans)<(-(2**31))):
            return -((2**31))
        if sign*int(ans)>(2**31-1):
            return 2**31-1
        return sign*int(ans)
            
                