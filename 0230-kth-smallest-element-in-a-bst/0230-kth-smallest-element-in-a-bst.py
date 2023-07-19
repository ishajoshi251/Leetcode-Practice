# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 1
        self.smallest = -1
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.count == k:
                self.smallest = root.val
            
            self.count +=1
            if self.count>k:
                return self.smallest
            inorder(root.right)
            
        inorder(root)
        return self.smallest