# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        inn = []
        
        self.inorder(root,inn)
        #print(inn)
        s = 0
        
        for i in inn:
            if i == low or i == high or (i>low and i<high):
                
                s += i
        return s
            
    def inorder(self,root,inn):
        if not root:
            return
        self.inorder(root.left,inn)
        inn.append(root.val)
        self.inorder(root.right,inn)
        