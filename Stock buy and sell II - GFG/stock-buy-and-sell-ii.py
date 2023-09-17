
from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, a : List[int]) -> int:
        # code here
        l=[]
        for i in range(n-1):
            if a[i]<a[i+1]:
                l.append(abs(a[i]-a[i+1]))
        return sum(l)



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends