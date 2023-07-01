"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next
            
        itr = head
        while itr:
            if itr.random != None:
                itr.next.random = itr.random.next
            itr = itr.next.next
        dummy = Node(0)
        ans = dummy
        itr = head
    
        while itr:
            ans.next = itr.next
            ans = ans.next
            itr.next = ans.next
            itr = itr.next
        return dummy.next
                