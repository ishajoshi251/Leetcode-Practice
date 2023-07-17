class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0 
        ten = 0  
        twenty = 0 
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            if bills[i] == 10:
                ten += 1
                if five>=1:
                    five -= 1
                else:
                    return False
            if bills[i] == 20:
                twenty += 1
                if ten>=1 and five>=1:
                    ten -= 1
                    five -= 1
                    continue
                elif ten == 0 and five>=3:
                    five -= 3
                
                else:
                    return False
        return True
                
            
            