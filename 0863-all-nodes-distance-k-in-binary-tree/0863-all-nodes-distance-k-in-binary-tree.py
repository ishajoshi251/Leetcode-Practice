# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findparent(self,mp,root):
        queue = [root]
        while queue:
            temp = queue.pop(0)
            if temp.left:
                mp[temp.left] = temp
                queue.append(temp.left)
            if temp.right:
                mp[temp.right] = temp
                queue.append(temp.right)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = {}
        self.findparent(d,root)

        vis = {}
        q = [target]
        vis[target] = True
        count = 0

        while q:
            n = len(q)
            if count == k:
                break
            count += 1
            for _ in range(n):
                temp = q.pop(0)
                if temp.left and not vis.get(temp.left):
                    q.append(temp.left)
                    vis[temp.left] = True
                if temp.right and not vis.get(temp.right):
                    q.append(temp.right)
                    vis[temp.right] = True
                if d.get(temp) and not vis.get(d[temp]):
                    q.append(d[temp])
                    vis[d[temp]] = True
        ans = []
        while q:
            ans.append(q.pop(0).val)     
        return ans