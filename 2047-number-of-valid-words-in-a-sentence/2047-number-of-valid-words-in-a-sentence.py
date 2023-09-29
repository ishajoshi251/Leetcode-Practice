class Solution:
    def countValidWords(self, s: str) -> int:

        v = []
        i = 0
        n = len(s)

        while i < n:
            temp = ""
            if s[i] != ' ':
                while i < n and s[i] != ' ':
                    temp += s[i]
                    i += 1
                v.append(temp)
            i += 1

        ans = 0

        for temp in v:
            c1 = 0
            c2 = 0
            flag = False

            for j in range(len(temp)):
                if temp[j].isdigit():
                    flag = True
                    break
                elif temp[0] == '-' or temp[-1] == '-':
                    flag = True
                    break
                elif temp[j] == '-':
                    c1 += 1
                    if c1 > 1:
                        flag = True
                        break
                if temp[j] in ['!', '.', ',']:
                    c2 += 1
                    if c2 > 1:
                        flag = True
                        break
                if (temp[j] in ['!', '.', ',']) and (j != len(temp) - 1):
                    flag = True
                    break
                if temp[j] == '-' and (
                        (j - 1 >= 0 and (not temp[j - 1].isalpha())) or
                        (j + 1 < len(temp) and (not temp[j + 1].isalpha()))):
                    flag = True
                    break

            if not flag:
                ans += 1

        return ans

