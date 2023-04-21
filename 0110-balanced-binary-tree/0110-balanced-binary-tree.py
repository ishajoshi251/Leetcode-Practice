# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = self.solve(root)
        if ans<0:
            return 0
        else:
            return 1
        
    def solve(self,root):
        if root is None:
            return 0
        lh = self.solve(root.left)
        rh = self.solve(root.right)
        
        if lh==-1:
            return -1
        if rh==-1:
            return -1
        if abs(lh-rh)>1:
            return -1
        return 1+max(lh,rh)