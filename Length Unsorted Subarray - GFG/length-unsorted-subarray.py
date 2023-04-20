#User function Template for python3
class Solution:

	def printUnsorted(self,arr, n):
		# cod
		if n == 1:
		    return [0,0]
	    i = 0
	    j = n-1
	    start = 0
	    end = 0
	    ans = []
	    while i<n-1:
	        if arr[i+1]<arr[i]:
	            start = i
	            break
	        i += 1
	    while j>0:
	        if arr[j-1]>arr[j]:
	            end = j
	            break
	        j -= 1
	    mini = min(arr[start:end+1])
	   
	    maxi = max(arr[start:end+1])
	    for i in range(n):
	        if arr[i]>mini:
	            ans.append(i)
	            break
	    for i in range(n-1,-1,-1):
	        if arr[i]<maxi:
	            ans.append(i)
	            break
	    return ans
	    
	    
	        
	    

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printUnsorted(arr, n)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends