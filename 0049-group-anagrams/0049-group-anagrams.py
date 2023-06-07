class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = {}
        for i in range(len(strs)):
            a = ' '.join(sorted(strs[i]))
            if a in d:
                d[a].append(strs[i])
            else:
                d[a] = [strs[i]]
        
        ans = []
        for key,values in d.items():
            ans.append(values)
        return ans