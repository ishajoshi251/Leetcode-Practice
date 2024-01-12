class Solution:
    def minimumSteps(self, s: str) -> int:
        i = j = count = 0
        n = len(s)
        s1 = list(s)
        while j<n:
            if s1[i] == '1' and s1[j] == '0':
                s1[i],s1[j] = s1[j],s1[i]
                
                count += j-i
                i += 1
            if s1[i] == '0':
                i += 1
            
                
            j += 1
        return count
    
    