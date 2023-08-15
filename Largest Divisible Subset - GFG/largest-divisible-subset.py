#User function Template for python3

class Solution:
    def LargestSubset(self, n, arr):
        #Code here
        dp = [1] * n
        hash_table = [0]*n
        ans = 1
        last_index = 0
        arr.sort()

        for i in range(n):
            hash_table[i] = i  # Initializing with current index
            for prev_index in range(i):
                if arr[i] % arr[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
                    hash_table[i] = prev_index
            if dp[i]>ans:
                ans=dp[i]
                last_index=i
        

        

        temp = [arr[last_index]]

        while hash_table[last_index] != last_index:  # Until not reach the initialization value
            last_index = hash_table[last_index]
            temp.append(arr[last_index])

        temp.reverse()
        return temp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.LargestSubset(n,arr)
        isValidSeq, sz = 1, len(res)
        for i in range(sz):
            for j in range(i + 1, sz):
                if (res[i] % res[j] == 0) or (res[j] % res[i] == 0):
                    continue
                else:
                    isValidSeq = 0
                    break
        print(isValidSeq, sz)
# } Driver Code Ends