class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        i = 0
        j = 0
        count = 0
        new = ''
        while j<len(num):
            new += num[j]
            if len(new)>k:
                new = new[1:]
                if len(new) == k and int(new) != 0:
                    if int(num)%int(new) == 0:
                        count += 1
            elif len(new) == k and int(new) != 0:
                if int(num)%int(new) == 0:
                    count += 1
                
            
            j += 1
        return count
                