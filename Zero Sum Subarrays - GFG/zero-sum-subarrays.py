#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
        d = {}
        count = 0
        l = []
        s = 0
        for i in range(n):
            s += arr[i]
            l.append(s)
        for i in range(n):
            if l[i] == 0:
                count += 1
            if l[i] not in d:
                d[l[i]] = 1
            else:
                count += d[l[i]]
                d[l[i]] += 1
                
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends