class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        count = [0] * 26
        vis = [0] * 26
        ans = []

        for i in range(n):
            count[ord(s[i]) - ord('a')] += 1

        for i in range(n):
            x = ord(s[i]) - ord('a')
            count[x] -= 1

            if vis[x] == 0:
                while ans and ans[-1] > s[i] and count[ord(ans[-1]) - ord('a')] > 0:
                    vis[ord(ans.pop()) - ord('a')] = 0
                ans.append(s[i])
                vis[x] = 1

        return ''.join(ans)