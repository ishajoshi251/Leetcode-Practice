#User function Template for python3

class Solution:
    def canEat(self,piles,H):
        hours = 0
        for i in piles:
            hours+= i//H
            if i%H != 0:
                hours += 1
        return hours
    def Solve(self, N, piles, H):
        # Code here
        ans = 0
        low = 1
        high = 10**9
        while low<=high:
            mid = (low+high)//2
            if self.canEat(piles,mid) <= H:
                high = mid-1
                ans = mid
            else:
                low = mid+1
                
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        piles = list(map(int, input().split()))
        H = int(input())
        ob = Solution()
        print(ob.Solve(N, piles, H))
# } Driver Code Ends