"""Return reference of new head of the reverse linked list
The input list will have at least one element
Node is defined as
​
class Node:
def __init__(self, data):
self.data = data
self.next = None
This is method only submission.
You only need to complete the method.
"""
class Solution:
def reverse(self,head, k):
# Code here
if head == None:
return None
prev = None
nextt = None
curr = head
count = 0
while (curr != None and count<k):
nextt = curr.next
curr.next = prev
prev = curr
curr = nextt
count += 1
if nextt != None:
head.next = self.reverse(nextt,k)
return prev
​
#{
# Driver Code Starts
class Node:
def __init__(self, data):
self.data = data
self.next = None
​
​
class LinkedList:
def __init__(self):
self.head = None