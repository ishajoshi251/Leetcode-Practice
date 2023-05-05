class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        s1 = 0
        s2 = 0
        i = 0
        j = 0
         
        while i<len(player1):
            if player1[i] == 10:
                count = 0 
                s1 += player1[i]
                i += 1
                while count<2 and i<len(player1):
                    s1 += player1[i]*2
                    count += 1
                    if player1[i] == 10:
                        count = 0
                    i += 1
            
                i -= 1
            else:
                s1 += player1[i]
            i += 1
        while j<len(player2):
            if player2[j] == 10:
                count = 0 
                s2 += player2[j]
                j += 1
                while count<2 and j<len(player2):
                    s2 += player2[j]*2
                    count += 1
                    if player2[j] == 10:
                        count = 0
                    j += 1
            
                j -= 1
            else:
                s2 += player2[j]
            j += 1   
        
        if s1>s2:
            return 1
        elif s1<s2:
            return 2
        else:
            return 0
                
            
                  
            
            
            
        
        