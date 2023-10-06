#User function Template for python3
class Solution:

	
	def search(self,p, s):
	    # code here
	    target = [0]*26
        for letter in p:
            target[ord(letter)-ord('a')] += 1
            
        count = [0]*26
        left = right = 0
        ret = []
        while right < len(s):
            count[ord(s[right])-ord('a')] += 1
            if right-left == len(p):
                count[ord(s[left])-ord('a')] -= 1
                left += 1
            if count == target:
                ret.append(left)
            right += 1
            
        return len(ret)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends