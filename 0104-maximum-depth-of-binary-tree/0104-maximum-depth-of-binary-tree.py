# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi = 0
    def dfs(self,root):
        if not root:
            return 0
        
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.maxi = max(l,r)
        return max(l,r)+1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.maxi+1