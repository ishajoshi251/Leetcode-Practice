class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        flag = False
        s = ""
        for i in range(len(num)-1,-1,-1):
            if num[i] == '0' and flag == False:
                continue
                
            else:
                flag = True
                s += num[i]
                
               
        return s[::-1]
        