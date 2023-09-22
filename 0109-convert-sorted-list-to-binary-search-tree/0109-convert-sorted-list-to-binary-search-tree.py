# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,head,tail):
        if head == tail:
            return None
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.solve(head,slow)
        root.right = self.solve(slow.next,tail)
            
        return root
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.solve(head,None)