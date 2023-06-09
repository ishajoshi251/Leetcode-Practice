class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low = 0 
        high = len(letters)-1
        while low <= high:
            mid = low +(high-low)//2
            if ord(str(letters[mid])) > ord(str(target)):      
                high = mid-1
            else:
                low = mid+1
        return letters[low%len(letters)]