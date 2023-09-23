class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        stack = []
        sign = '+'
        ans = 0
        curr = 0
        for i in range(len(s)):
            if s[i]>='0' and s[i]<='9':
                curr= curr*10 + int(s[i])
            elif s[i] == '+' or s[i] == '-' or s[i] == '/' or s[i] == '*':
                if sign == '+':
                    stack.append(curr)
                if sign == '-':
                    stack.append(-1*curr)
                if sign == '*':
                    num = stack.pop()
                    stack.append(num*curr)
                if sign == '/':
                    num = stack.pop()
                    stack.append(int(num/curr))
                    
                sign = s[i]
                curr = 0
              
        while stack:
            ans += stack.pop()
        return ans