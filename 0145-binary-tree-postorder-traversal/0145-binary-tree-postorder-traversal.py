# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s1 = []
        s1.append(root)
        s2 = []
        ans = []
        while s1:
            temp = s1.pop()
            s2.append(temp)
            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)
        while s2:
            temp = s2.pop()
            ans.append(temp.val)
        return ans