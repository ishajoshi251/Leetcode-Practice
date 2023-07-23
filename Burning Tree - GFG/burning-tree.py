#User function Template for python3

class Solution:
    def Find_Parent(self,root, mp):
        queue = [root]
        while queue:
            temp = queue.pop(0)
            if temp.left:
                mp[temp.left] = temp
                queue.append(temp.left)
            if temp.right:
                mp[temp.right] = temp
                queue.append(temp.right)
    def find(self,root, target):
        if not root:
            return None
        if root.data == target:
            return root
        left_result = self.find(root.left, target)
        if left_result:
            return left_result
        return self.find(root.right, target)
    def minTime(self, root,target):
        # code here
        mp = {}
        self.Find_Parent(root, mp)
    
        f = self.find(root, target)
        if not f:
            return -1
    
        vis = {}
        q = [f]
        timee = 0
        vis[f] = True
        while q:
            size = len(q)
            timee += 1
            flag = False
    
            for _ in range(size):
                temp = q.pop(0)
                if temp.left and not vis.get(temp.left):
                    vis[temp.left] = True
                    q.append(temp.left)
                    flag = True
                if temp.right and not vis.get(temp.right):
                    vis[temp.right] = True
                    q.append(temp.right)
                    flag = True
                if mp.get(temp) and not vis.get(mp[temp]):
                    vis[mp[temp]] = True
                    q.append(mp[temp])
                    flag = True
    
            if not flag:
                break
    
        return timee - 1



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
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends