#User function Template for python3

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self,X):
        # code here
        self.stack1.append(X)
        
    def dequeue(self):
        # code here
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ans
            

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        ob=Queue()
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                ob.enqueue(a[i+1])
                i+=1
            else:
                print(ob.dequeue(),end=" ")
            i+=1

        print()
# } Driver Code Ends