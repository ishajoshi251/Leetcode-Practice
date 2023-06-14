class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]
        heights.sort(reverse = True)
        for height in heights:
            ans.append(d[height])
        return ans
        