class Solution:
    def minOperations(self, nums: List[int]) -> int:
       
        d = {}
        n = len(nums)
        mini = 0
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i in d:
            if d[i] == 1:
                return -1
            if d[i] == 4:
                mini += 2
                continue
            
            while d[i] >= 3:
                if d[i]%3 == 0:
                    mini += d[i]//3
                    d[i] = 1
                    break
                if d[i]-3>=2:
                    d[i] -= 3
                    mini += 1
                else:
                    break
                
                
                
            while d[i]>=2:
                if d[i]%2 == 0:
                    mini += d[i]//2
                    break
                else:
                    return -1
              
                     
            
       
            
        return mini
        