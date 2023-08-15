class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        n = len(arr)
    
        # Sort the array
        arr.sort()

        dp = [1] * n
        hash_table = list(range(n))

        for i in range(n):
            hash_table[i] = i  # Initializing with current index
            for prev_index in range(i):
                if arr[i] % arr[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
                    hash_table[i] = prev_index
        ans = -1
        last_index = -1

        for i in range(n):
            if dp[i] > ans:
                ans = dp[i]
                last_index = i

        temp = [arr[last_index]]

        while hash_table[last_index] != last_index:  # Until not reach the initialization value
            last_index = hash_table[last_index]
            temp.append(arr[last_index])

        temp.reverse()
        return temp