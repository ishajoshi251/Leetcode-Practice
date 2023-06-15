
class Solution:
    def arrayRepresentHeap(self,arr,n):
        # Your code goes here            
        m=(n-1)//2
        for i in range(m+1):
            if (i*2+1)<n:
                if arr[i]<arr[i*2+1]:
                    return 0
            if (i*2+2)<n:
                if arr[i]<arr[i*2+2]:
                    return 0
        return 1


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(ob.arrayRepresentHeap(arr,n))
# } Driver Code Ends