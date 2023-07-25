class Solution:
	def wordLadderLength(self, start, target, wordList):
		#Code here
        s = set(wordList)
        q = []
        q.append([start,1])
        while q:
            word,step = q.pop(0)
            if word == target:
                return step
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new = word[:i]+ch+word[i+1:]
                    if new in s:
                        s.remove(new)
                        q.append([new,step+1])
        return 0

#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends