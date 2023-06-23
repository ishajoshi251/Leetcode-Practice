#User function Template for python3

class Solution:
    def func(self,x):
        if x % 4 == 0:
            return x
        elif x % 4 == 1:
            return 1
        elif x % 4 == 2:
            return x + 1
        elif x % 4 == 3:
            return 0

    def findXOR(self,l, r):
        return self.func(l - 1) ^ self.func(r)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        l, r = list(map(int, input().split()))
        ob = Solution()
        res = ob.findXOR(l, r)
        print(res)
# } Driver Code Ends