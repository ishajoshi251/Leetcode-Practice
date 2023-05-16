# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if head and not head.next:
            return head
        prev = head
        curr = head.next
        while curr.next and curr.next.next:
            prev.val,curr.val = curr.val,prev.val
            prev = prev.next.next
            curr = curr.next.next
        prev.val,curr.val = curr.val,prev.val
        return head