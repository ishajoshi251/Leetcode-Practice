# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        2 4 7 8 9    5 -  3 = 2
        
        itr = head
        while itr.next != None:
            itr = itr.next
        itr.next = head
        count = 0
        while count < k:
            itr = itr.next
            count += 1
        head = itr.next
        itr.next = None
        return head
        

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        itr = head
        while itr.next:
            itr = itr.next
        itr.next = head
        ptr = head
        count = 0
        while count<k-1:
            ptr = ptr.next
            count += 1
        head = ptr.next
        ptr.next = None
        return head



#{ 
 # Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = Solution().rotate(lis.head,k)
        printList(head)
# } Driver Code Ends