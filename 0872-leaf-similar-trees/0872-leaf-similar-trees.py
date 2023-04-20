# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        s1 = []
        s2 = []
        
        def dfs(root,s):
            if not root:
                return 
            if not root.left and not root.right:
                s.append(root.val)
            dfs(root.left,s)
            dfs(root.right,s)
        dfs(root1,s1)
        dfs(root2,s2)
                
        return s1 == s2