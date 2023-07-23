#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        class Solution:
    def findparent(self,d,root):
        q = []
        q.append(root)
        while q:
            temp = q.pop(0)
            if temp.left:
                d[temp.left] = temp
                q.append(temp.left)
            if temp.right:
                d[temp.right] = temp
                q.append(temp.right)
    def KDistanceNodes(self,root,target,k):
        # code here
        # return the sorted list all nodes at k distance from target
        d = {}
        self.findparent(d,root)
        q = []
        q.append(target)
        vis = {}
        vis[target] = True
        count = 0
        while q:
            n = len(q)
            if count == k:
                break
            count += 1
            for i in range(n):
                temp = q.pop(0)
                if temp.left and not vis.get(temp.left):
                    vis[temp.left] = True
                    q.append(temp.left)
                if temp.right and not vis.get(temp.right):
                    vis[temp.right] = True
                    q.append(temp.right)
                if d[temp] and not vis.get(d[temp]):
                    vis[d[temp]] = True
                    q.append(d[temp])
        ans = []
        while q:
            temp = q.pop(0)
            ans.append(temp.data)
        return sorted(ans)
'''

class Solution:
    
    def KDistanceNodes(self,root,target,k):
        # code here
        # return the sorted list all nodes at k distance from target
        dct = {}
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()  # popping out the first element
                if node.data == target:
                    Target = node
                if node.left:   # if the left child exist 
                    dct[node.left] = node   # adding the child--> parent
                    q.append(node.left)   # appending the child into the queue
                if node.right:     # same if the right child exist 
                    dct[node.right] = node
                    q.append(node.right)
        vis = set()
        pq = deque([Target])
        ds = 0
        while ds != k:
            for i in range(len(pq)):
                node = pq.popleft()
                vis.add(node)
                if node.left not in vis and node.left:
                    pq.append(node.left)
                    vis.add(node.left)
                if node.right not in vis and node.right:
                    pq.append(node.right)
                    vis.add(node.right)
                if dct.get(node)!=None and dct[node] not in vis:
                    pq.append(dct[node])
                    vis.add(dct[node])
            ds += 1
        ans = []
        while pq:
            ans.append(pq.pop().data)
        ans.sort()
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends