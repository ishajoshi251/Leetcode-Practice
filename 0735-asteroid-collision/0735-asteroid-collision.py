class Solution(object):
    def asteroidCollision(self, ast):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # 5 7 9 11 13 -2 10 -10 2 3 -7
        stack = []
        ans = []
        for i in range(len(ast)):
            if ast[i]>0:
                stack.append(ast[i])
            else:
                while stack and  stack[-1]<-1*ast[i]:
                    stack.pop()
                if stack and stack[-1] == -1*ast[i]:
                    stack.pop()
                    continue
                if len(stack) == 0:
                    ans.append(ast[i])
        while stack:
            ans.append(stack[0])
            stack.pop(0)
            
        return ans
                    