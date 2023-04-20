# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = []                        
        q.append([root,0])
        maxi = 1
        while q:
             n = len(q)
             a = q[0][1]
             b = q[-1][1]
             maxi = max(maxi,b-a+1)
             while n:
                node = q[0][0]
                i = q[0][1]
                q.pop(0)
                
                if node.left:
                    q.append([node.left,2*i+1])
                    
                if node.right:
                    q.append([node.right,2*i+2])
                    
                    
                        
                n -= 1
        return maxi
                
             
        