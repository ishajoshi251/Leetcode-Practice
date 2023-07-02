# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(sef,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        ans = dummy
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return ans.next
    
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeList(l1,l2)