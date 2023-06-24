class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp = ''
        for i in words:
            temp += i
            if s == temp:
                return True
        return False