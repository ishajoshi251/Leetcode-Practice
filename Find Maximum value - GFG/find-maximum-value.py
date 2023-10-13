'''The function returns an integer
which denotes the max value 
of abs(i â€“ j) * min(arr[i], arr[j]) 
in the array.'''
# You are required to complete this method
# You may use module's
class Solution:
    def max_val(self, arr, n):
        # code here
       ans=[]
       i=0
       j=n-1
       while(i<j):
           res=(abs(i-j)*min(arr[i],arr[j]))
           ans.append(res)
           if(arr[i]<arr[j]):
               i+=1
           else:
               j-=1
       return max(ans)

#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().max_val(arr, n))
# } Driver Code Ends