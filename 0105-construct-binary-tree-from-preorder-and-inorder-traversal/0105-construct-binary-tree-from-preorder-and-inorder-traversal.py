# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.idx = 0
    def constructTree(self,preorder,inorder, low,high, mp):
        if low>high:
            return None
        root = TreeNode(preorder[self.idx])
        self.idx+=1
        if high == low:
            return root
        mid = mp[root.val]
        root.left = self.constructTree(preorder,inorder,low,mid-1, mp)
        root.right = self.constructTree(preorder,inorder,mid+1,high, mp)
        return root
    
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
         
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i
        
        return self.constructTree(preorder,inorder,0,len(inorder)-1, mp)

