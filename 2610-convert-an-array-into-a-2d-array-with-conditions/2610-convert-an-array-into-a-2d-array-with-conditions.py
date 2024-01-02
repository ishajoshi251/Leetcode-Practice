class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        '''
        ans = []
        d = {}
       
        l = 0
        while l != len(nums):
            row = []
            count = 0
            for i in nums:
                if i in d:
                    continue
                else:
                    count += 1
                    d[i] = 1
                    row.append(i)
            ans.append(row)
            d.clear()
            l += count
        return ans
        '''
        
        freq = [0] * (len(nums) + 1)
        ans = []

        for c in nums:
            if freq[c] >= len(ans):
                ans.append([])

            # Store the integer in the list corresponding to its current frequency.
            ans[freq[c]].append(c)
            freq[c] += 1

        return ans
