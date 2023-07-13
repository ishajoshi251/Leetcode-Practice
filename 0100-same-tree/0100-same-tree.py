# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if (p and not q) or (not p and q):
            return False
        q1 = []
        q2 = []
        q1.append(p)
        q2.append(q)
        while q1:
            n = len(q1)
            m = len(q2)
            if n != m:
                return False
            while n:
                t1 = q1.pop(0)
                t2 = q2.pop(0)
                if t1.val != t2.val:
                    return False
                if t1.left and t2.left:
                    q1.append(t1.left)
                    q2.append(t2.left)
                if t1.right and t2.right:
                    q1.append(t1.right)
                    q2.append(t2.right)
                if t1.left and not t2.left:
                    return False
                if t2.left and not t1.left:
                    return False
                if t1.right and not t2.right:
                    return False
                if t2.right and not t1.right:
                    return False
                n -= 1
        return True
            