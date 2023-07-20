# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,first,last,middle,prev):
        if root:
            self.solve(root.left,first,last,middle,prev)
            if prev[0] and prev[0].val>root.val:
                if not first[0]:
                    first[0] = prev[0]
                    middle[0] = root
                else:
                    last[0] = root
            prev[0] = root
            
                    
            self.solve(root.right,first,last,middle,prev)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = [None]
        last = [None]
        middle=[None]
        prev = [None]
        self.solve(root,first,last,middle,prev)
        if last[0] and first[0]:
            last[0].val,first[0].val = first[0].val,last[0].val
        else:
            middle[0].val,first[0].val = first[0].val,middle[0].val
        