# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None or k == 0:
            return head

        cur = head
        length = 1

        while cur.next:  # count length
            cur = cur.next
            length += 1

        cur.next = head
        k = k % length  # if k > length
        k = length - k

        temp = head

        i = 1
        while i < k:  # find len-kth node
            temp = temp.next
            i += 1

        head = temp.next
        temp.next = None

        return head
