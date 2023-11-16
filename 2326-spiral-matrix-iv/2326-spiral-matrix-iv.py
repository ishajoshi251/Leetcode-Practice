# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
       

        dp = [[-1 for j in range(n)] for i in range(m)]
        top = left = 0
        flag = False
        bottom = m - 1
        right = n - 1
        while top <= bottom and left <= right and head:
            # Traverse from left to right
            for i in range(left, right + 1):
                dp[top][i] = head.val
                head = head.next
                if not head:
                    flag = True
                    break
            if flag:
                break
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                dp[i][right] = head.val
                head = head.next
                if not head:
                    flag = True
                    break
            if flag:
                break
            right -= 1

            # Traverse from right to left
            for i in range(right, left - 1, -1):
                dp[bottom][i] = head.val
                head = head.next
                if not head:
                    flag = True
                    break
            if flag:
                break
            bottom -= 1

            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                dp[i][left] = head.val
                head = head.next
                if not head:
                    flag = True
                    break
            if flag:
                break
            left += 1

        return dp


