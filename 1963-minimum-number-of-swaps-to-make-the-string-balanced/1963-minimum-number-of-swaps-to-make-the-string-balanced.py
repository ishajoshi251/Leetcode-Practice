class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in s:
            if i == '[':
                stack.append('[')
            else:
                if stack:
                    stack.pop()
        return (len(stack)+1)//2