# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxi = 0
        
        def solve(node, goleft, currlength):
            
            
            if not node:
                return
            
            self.maxi = max(self.maxi, currlength)
            
            if goleft:
                solve(node.left, False, currlength + 1)
                solve(node.right, True, 1)
            else:
                solve(node.right, True, currlength + 1)
                solve(node.left, False, 1)
        
        solve(root, True, 0)
        solve(root, False, 0)
        
        return self.maxi
           