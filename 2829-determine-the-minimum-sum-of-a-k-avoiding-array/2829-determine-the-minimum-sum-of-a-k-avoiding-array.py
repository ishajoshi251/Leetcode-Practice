class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        arr = []
        i = 1
        
        while n:
            if k-i in arr:
                i+= 1
                continue
            else:
                arr.append(i)
                i += 1
                n-=1
        return sum(arr)