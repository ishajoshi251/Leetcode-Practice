class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 1
        j = len(skill)-2
        s = skill[0]*skill[-1]
        c = skill[0]+skill[-1]
        while i<j:
            if skill[i]+skill[j] == c:
                s += skill[i]*skill[j]
                i += 1
                j -= 1
            else:
                return -1
        return s
            