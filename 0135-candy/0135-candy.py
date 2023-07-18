class Solution:
    def candy(self, ratings: List[int]) -> int:
        count = [1]*len(ratings)
        if len(ratings) == 1:
            return 1
        if len(ratings) == 2:
            if ratings[0]!=ratings[1]:
                return sum(count)+1
            else:
                return sum(count)
        
                
        for i in range(1,len(ratings)):
            if ratings[i-1] < ratings[i]:
                count[i] = count[i-1]+1
                
        count2=[1]*len(ratings)
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                count2[i] = count2[i+1]+1
                
        
    
        s = 0
        for i in range(len(ratings)):
            s += max(count[i],count2[i])
            
                
                
            
        return s
        
            
        
      
       