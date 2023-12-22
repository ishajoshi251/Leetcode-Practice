class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ans=0
        vowel_list=['a','e','i','o','u']
        for i in range(len(s)):
            vowels,contants=0,0
            # We have to take the 1st element as well
            j=i
            while j<len(s):
                if s[j] in vowel_list:
                    vowels+=1
                else:
                    contants+=1
                if vowels == contants and (vowels*contants) %k==0:
                    ans+=1
                j+=1
        return ans