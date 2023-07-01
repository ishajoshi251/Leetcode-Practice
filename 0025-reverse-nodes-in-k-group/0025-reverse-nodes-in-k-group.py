# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        curr = head

        while cnt < k and curr:
            curr = curr.next
            cnt += 1

        if cnt < k:
            return head
        if not head:
            return None
        curr = head
        prev= None
        nxt = None
        count = 0
        while curr and count<k:
            nxt = curr.next
            curr.next = prev
            prev= curr
            curr = nxt
            count += 1
        if nxt != None:
            head.next = self.reverseKGroup(nxt,k)
        return prev
        