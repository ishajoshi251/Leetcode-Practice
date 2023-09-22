# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,targetSum,s):
        if not root:
            return False
        s += root.val
        if not root.left and not root.right:
            if s == targetSum:
                return True
        l =self.solve(root.left,targetSum,s)
        r = self.solve(root.right,targetSum,s)
        return l or r
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.solve(root,targetSum,0)
        