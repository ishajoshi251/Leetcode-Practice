# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        def solve(root,targetSum,s,ans,temp):
            if not root:
                return 

            s += root.val
            temp.append(root.val)

            if not root.left and not root.right:
                if  s == targetSum:
                    ans.append(temp[:])
                    
            solve(root.left,targetSum,s,ans,temp)
            solve(root.right,targetSum,s,ans,temp)
            temp.pop()
        ans = []
        temp = []
        solve(root,targetSum,0,ans,temp)
        return ans