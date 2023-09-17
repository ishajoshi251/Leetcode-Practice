#User function Template for python3

class Solution:
    def combinationSum(self, K, target):
        # Code here
        from itertools import combinations
        l = []
        com = combinations(range(1,10), K)
        for i in com:
            if sum(i)==target:
                l.append(i)
                
        return l
 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        K, N = list(map(int, input().split()))
        ob = Solution()
        ans = ob.combinationSum(K, N)
        for combination in ans:
            for val in combination:
                print(val, end = ' ')
            print()
# } Driver Code Ends