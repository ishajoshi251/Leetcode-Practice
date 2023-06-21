#User function Template for python3

class Solution:
    def isPossible(self,stalls,n,k,mid):
        count = 1
        tep = stalls[0]
        for i in range(n):
            if stalls[i]-tep>=mid:
                tep = stalls[i]
                count += 1
            if count == k:
                return True
        return False
    def solve(self,n,k,stalls):
        stalls.sort()
        low = 1
        high = stalls[-1]-stalls[0]
        ans = -1

        while low<=high:
            mid = low+(high-low)//2
            if self.isPossible(stalls,n,k,mid):
                ans = mid
                low =mid+1
            else:
                high = mid-1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends