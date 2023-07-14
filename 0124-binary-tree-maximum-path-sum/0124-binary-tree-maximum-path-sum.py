# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi = -111111111
    def dfs(self,root):
        if not root:
            return 0
        l = max(0,self.dfs(root.left))
        r = max(0,self.dfs(root.right))
        self.maxi = max(self.maxi,l+r+root.val)
        return max(l,r)+root.val
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        self.dfs(root)
        return self.maxi