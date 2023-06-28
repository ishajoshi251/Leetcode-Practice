class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in num:
            while stack and k>0 and i<stack[-1]:
                stack.pop()
                k -= 1
            if len(stack)!=0 or i != '0':
                stack.append(i)
        while stack and k>0:
            stack.pop()
            k -= 1
        if len(stack) == 0:
            return '0'
        return ''.join(stack)
            
            
        