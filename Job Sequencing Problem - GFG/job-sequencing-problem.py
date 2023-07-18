#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        '''
        1   2  3   4
        4   1  1   1 
        20  10 40  30
        
        
        1    1    4    1
        40   30   20   10
    
        
        vis=[1 0 0 1 0]
        '''
        
        Jobs.sort(key=lambda x:x.profit,reverse=True)
        profit = 0
        time = 0
        vis = [0]*(n)
        for i in range(n):
            for j in range(Jobs[i].deadline-1,-1,-1):
                if vis[j] == 0:
                    vis[j] += 1
                    time += 1
                    profit += Jobs[i].profit
                    break
            
            
        return [time,profit]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends