import heapq
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        m = len(searchWord)
        ans = []
        s = ""
        for i in range(m):
            s += searchWord[i]
            pq = []
            for j in range(n):
                temp = []
                s2 = products[j]
                a = 0
                while a<len(s) and a<len(s2) and s[a] == s2[a]:
                    a += 1
                if a == len(s):
                    heapq.heappush(pq,s2)
            x = 3
            while pq and x>0:
                temp.append(heapq.heappop(pq))
                x -= 1
            ans.append(temp)
        return ans