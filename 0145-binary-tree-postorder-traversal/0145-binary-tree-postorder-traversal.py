# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,root,ans):
        if not root:
            return
        
        self.dfs(root.left,ans)
        
        self.dfs(root.right,ans)
        ans.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        self.dfs(root,ans)
        return ans