#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        arr = []
        for i in range(n):
            arr.append([start[i],end[i]])
        arr.sort(key=lambda x:x[1])
        count =1
        i = 0
        for j in range(1,n):
            if arr[j][0]>arr[i][1]:
                count += 1
                i = j
        return count
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends