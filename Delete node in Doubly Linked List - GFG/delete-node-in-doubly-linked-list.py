#User function Template for python3

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteNode(self,head, x):
        # Code here
        count = 1
        itr = head
        if x == count:
           head= head.next
           head.prev = None
        else:
            while itr:
                if count == x:
                    itr.prev.next = itr.next
                itr = itr.next
                count += 1
        return head
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        pos = int(input())
        Solution().deleteNode(llist.head, pos)
        llist.printList(llist.head)
# Contributed by: Harshit Sidhwa

                               
# } Driver Code Ends