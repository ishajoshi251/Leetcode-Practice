#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        five = 0
        ten = 0
        twenty = 0
        for i in range(N):
            if bills[i] == 5:
                five += 1
            if bills[i] == 10:
                ten += 1
                if five>=1:
                    five -= 1
                else:
                    return False
            if bills[i] == 20:
                twenty += 1
                if ten>=1 and five>=1:
                    ten -= 1
                    five -= 1
                    continue
                elif ten ==0 and five>=3:
                    five -= 3
                else:
                    return False
        return True

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends