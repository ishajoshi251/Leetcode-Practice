import heapq
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def __init__(self):
        self.q = []
    def Sorted(self, s):
        # Code here
        
        if len(s) == 0:
            return 
        heapq.heappush(self.q,s.pop())
        self.Sorted(s)
        while self.q:
            s.append(heapq.heappop(self.q))
        return s

#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends