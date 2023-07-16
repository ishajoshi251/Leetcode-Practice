# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,ans,level):
        if not root:
            return
        if len(ans) == level:
            ans.append(root.val)
        self.solve(root.right,ans,level+1)
        self.solve(root.left,ans,level+1)
        
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        self.solve(root,ans,0)
        return ans