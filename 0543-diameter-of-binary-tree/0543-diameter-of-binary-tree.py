# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l = 0
    def dfs(self,root):
        if not root:
            return 0
        le = self.dfs(root.left)
        ri = self.dfs(root.right)
        self.l = max(self.l,le+ri)
        return max(le,ri)+1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.l
        
        