#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def reverse(self,head):
        curr= head
        nxt = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        if not first:
            return second
        if not second:
            return first
        dummy = Node(0)
        ans = dummy
        carry = 0
        temp1 = self.reverse(first)
        temp2 = self.reverse(second)
        
        while temp1 and temp2:
            summ = temp1.data+temp2.data+carry
            carry = summ//10
            dummy.next = Node(summ%10)
            temp1 = temp1.next
            temp2 = temp2.next
            dummy = dummy.next
            
        while temp1:
            summ = temp1.data+carry
            carry = summ//10
            dummy.next = Node(summ%10)
            temp1 = temp1.next
            dummy = dummy.next
            
        while temp2:
            summ = temp2.data+carry
            carry = summ//10
            dummy.next = Node(summ%10)
            temp2 = temp2.next
            dummy = dummy.next
            
        if carry:
            dummy.next = Node(1)
        
        res = self.reverse(ans.next)
        return res
            
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends