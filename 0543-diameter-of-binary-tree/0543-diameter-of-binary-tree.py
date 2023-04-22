# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    dia = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return True
        self.height(root)
        return self.dia

    def height(self, root):
        if (root == None): return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if l+r > self.dia:
            self.dia = l+r
        return max(l, r)+1