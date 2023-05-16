# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        
        count = 0
        ptr  = head
        itr = head
        
        while ptr:
            if count == k-1:
                temp = ptr
            count += 1
            ptr = ptr.next
            
        i = count-k
        while i-1:
            itr = itr.next
            i -= 1
            
        itr.next.val,temp.next.val = temp.next.val,itr.next.val 
        return head
        """
        ptr1 = head
        ptr2 = head
        temp = None
        
        count = 0
    
        while ptr1:
            if count == k-1:
                temp = ptr1
            count += 1
            ptr1 = ptr1.next
    
        z = count - k
        while z:
            ptr2 = ptr2.next
            z -= 1
    
        temp.val, ptr2.val = ptr2.val, temp.val
        return head

            
        