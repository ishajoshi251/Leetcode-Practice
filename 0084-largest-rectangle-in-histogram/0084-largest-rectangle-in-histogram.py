class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        
        brute force: N^2
        width*height = area
        (right smaller-left smaller+1)*a[i]
        maxi = max(maxi,area)
        
        
        optimal using stack: N
        left_smaller = 0      0          2(stack.top+1)    3      2     5
                       0->2   pop        2->5              3->6   pop   5->3
                              1->1       1->1              2->5   pop   4->2
                                                           1->1   4->2  1->1
                                                                  1->1
        left_smaller = [0,0,2,3,2,5]
        
        right_smaller =  0      5          3         3(stack.top()-1)    5      5
                         0->2   1->1       pop       3->6                pop    5->3                                                 3->5      4->2                 4->2                4->2  
       left_smaller = [0,0,2,3,2,5]                
       right = [0,5,3,3,5,5]
       area = []       right-left+1 * a[i]
       0-0+1*2 = 2
       5-0+1*1 = 6
       3-2+1*5 = 10
       3-3+1*6 = 6
       5-2+1*2 = 8
       5-5+1*3 = 3
       
                                                
        """
        n = len(heights)
        nsr = [0] * n
        nsl = [0] * n

        s = []

        for i in range(n - 1, -1, -1):
            while s and heights[i] <= heights[s[-1]]:
                s.pop()
            if not s:
                nsr[i] = n
            else:
                nsr[i] = s[-1]
            s.append(i)

        while s:
            s.pop()

        for i in range(n):
            while s and heights[i] <= heights[s[-1]]:
                s.pop()
            if not s:
                nsl[i] = -1
            else:
                nsl[i] = s[-1]
            s.append(i)

        ans = 0

        for i in range(n):
            ans = max(ans, heights[i] * (nsr[i] - nsl[i] - 1))
        return ans

        