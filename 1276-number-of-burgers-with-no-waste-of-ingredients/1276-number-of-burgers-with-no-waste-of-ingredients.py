class Solution(object):
    def numOfBurgers(self, tomato, cheese):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if tomato == 0 and cheese == 0:
            return [0,0]
        if tomato%2 != 0:
            return []
        if tomato<=cheese:
            return []
        
        ans = []
        
        
        four=(tomato-2*cheese)//2  # no of jumbo burgers by solving 4x+2y=t and x+y=c
        two=cheese-four #number of small burgers
        if four>=0 and two>=0 and (4*four+2*two == tomato):
            
            ans.append(four)
            ans.append(two)
        return ans
        