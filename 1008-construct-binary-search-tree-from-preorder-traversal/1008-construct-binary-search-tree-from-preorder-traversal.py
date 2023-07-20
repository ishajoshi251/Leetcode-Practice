# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,preorder,i,maxi):
        if i[0] == len(preorder) or preorder[i[0]]>maxi:
            return None
        root = TreeNode(preorder[i[0]])
        i[0]+=1
        root.left = self.helper(preorder,i,root.val)
        root.right = self.helper(preorder,i,maxi)
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = [0]
        return self.helper(preorder,i,float('inf'))
    

