class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = []
        for i in range(1,n+1):
            if n % i == 0:
                res.append(i)
        if len(res)<k:
            return -1
        else:
            return res[k-1]
            
        