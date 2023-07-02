#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
if not head:
            return None
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next
            
        itr = head
        while itr:
            if itr.random != None:
                itr.next.random = itr.random.next
            itr = itr.next.next
        dummy = Node(0)
        ans = dummy
        itr = head
    
        while itr:
            ans.next = itr.next   1* 2*
            ans = ans.next        1* 2*
            itr.next = ans.next   2 3
            itr = itr.next        2 3
        return dummy.next
                
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        if not head:
            return None
        
        curr = head
        while curr:
            new = Node(curr.data)  #1*
            new.next = curr.next  #1*->2
            curr.next = new       #1->1*   
            curr = curr.next.next #1->->2
        
        itr = head
        while itr:
            if itr.arb != None:
                itr.next.arb = itr.arb.next
            itr = itr.next.next
        
        dummy = Node(0)
        ans = dummy
        itr = head
        while itr:
            ans.next = itr.next
            ans = ans.next
            itr.next = ans.next
            itr = itr.next
        return dummy.next



#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
class LinkedList:
    def __init__(self):
        self.head = None

def insert(tail,data):
    tail.next=Node(data)
    return tail.next
    

def setarb(head,a,b):
    h=head
    i=1
    while i<a and h:
        h=h.next
        i+=1
    an=h
    
    h=head
    i=1
    while i<b and h:
        h=h.next
        i+=1
        
    if an:
        an.arb=h
        
def validation(head,res):
    
    headp = head
    resp = res
    
    d = {}
    
    while head and res:
        if head==res:
            return
        if head.data != res.data:
            return
        
        if head.arb:
            if not res.arb:
                return
            
            if head.arb.data != res.arb.data:
                return
            
        elif res.arb:
            return
        if head not in d:
            d[head] = res
        head=head.next
        res=res.next
        
    if not head and res:
        return
    elif head and not res:
        return
    
    head = headp
    res = resp
    while head:
        if head == res:
            return 
        if head.arb:
            if head.arb not in d:
                return
            if d[head.arb] != res.arb:
                return
        head=head.next
        res=res.next
        
    return True


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        __n,__m = list(map(int, input().strip().split()))
        __nodes = list(map(int, input().strip().split()))
        __aarb = list(map(int, input().strip().split()))
        __ll=LinkedList()
        __ll2=LinkedList()
        __ll.head=Node(__nodes[0])
        __ll2.head=Node(__nodes[0])
        __tail=__ll.head
        __tail2=__ll2.head
        
        for x in __nodes[1:]:
            __tail=insert(__tail,x)
            __tail2=insert(__tail2,x)
        
        for i in range(0,len(__aarb),2):
            setarb(__ll.head,__aarb[i],__aarb[i+1])
            setarb(__ll2.head,__aarb[i],__aarb[i+1])
        
        obj = Solution()
        __res=obj.copyList(__ll.head)
        if validation(__ll.head,__res) and validation(__ll2.head,__res):
            print(1)
        else:
            print(0)
# } Driver Code Ends