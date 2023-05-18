# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        Next = None
        curr = slow
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        summ= 0
        while prev:
            summ = max(summ,head.val+prev.val)
            head = head.next
            prev = prev.next
        return summ
        
            
            
            
            