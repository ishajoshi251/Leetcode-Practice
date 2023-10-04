# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        # If either left or right child is None, return the non-None depth + 1
        if root.left is None or root.right is None:
            return max(left_depth, right_depth) + 1
        # Otherwise, return the minimum depth + 1
        return min(left_depth, right_depth) + 1