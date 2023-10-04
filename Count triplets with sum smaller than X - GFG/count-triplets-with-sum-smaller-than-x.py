class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        arr.sort()
        c = 0
        for i in range(0,n-1):
            j = i+1
            k = n-1
            while j<k:
                if (arr[i]+arr[j]+arr[k])<sumo:
                    c+=(k-j)
                    j+=1
                else:
                    k-=1
        return c

#{ 
 # Driver Code Starts

t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    k=l[1]
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.countTriplets(a,n,k)
    print(ans)
# } Driver Code Ends