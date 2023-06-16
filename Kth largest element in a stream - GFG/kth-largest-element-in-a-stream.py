#User function Template for python3
import heapq
class Solution:
    def kthLargest(self, k, arr, n):
        # code here 
        heap = []
        ans = []
        for i in range(n):
            heapq.heappush(heap,arr[i])
            if len(heap)<k:
               
                ans.append(-1)
            elif len(heap)==k:
                ans.append(heap[0])
            else:
                heapq.heappop(heap)
                ans.append(heap[0])
        return ans       
                
                
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        k,n=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(*ob.kthLargest(k,arr,n))
# } Driver Code Ends