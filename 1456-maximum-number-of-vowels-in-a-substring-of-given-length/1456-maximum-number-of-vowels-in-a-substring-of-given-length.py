class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxi =count=i=j= 0
        
        while j<len(s):
            if s[j] in ['a','e','i','o','u']:
                count += 1
            if j-i+1<k:
                j+=1
                continue
            elif j-i+1 == k:
                maxi = max(maxi,count)
            else:
                while j-i+1>k:
                    if s[i] in ['a','e','i','o','u']:
                        count -= 1
                    i += 1
                maxi = max(maxi,count)
                    
            j += 1
        
        
        return maxi
                    
                    
            
        
        