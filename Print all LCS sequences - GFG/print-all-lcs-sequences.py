#User function Template for python3

class Solution:
	def all_longest_common_subsequences(self, s, t):
		# Code here
        n,m = len(s),len(t)
		dp = [[0]*(m+1) for _ in range(n+1)]
		for i in range(1,n+1):
		    for j in range(1,m+1):
    		    if s[i-1] == t[j-1]:
    		        dp[i][j] = 1 + dp[i-1][j-1]
    		    else:
    		        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
		 
		res=[]
        
        self.process(s,t,0,0,dp[n][m],"",res,n,m)
        res=list(set(res))
        res.sort()
        return res
    
    def process(self,s1,s2,ind1,ind2,lcslen,curlcs,res,x,y):
        if len(curlcs)==lcslen:
            res.append(curlcs)
            return
        if ind1 >=x or ind2>=y:return
        
        for i in range(ind1,x,1):
            for j in range(ind2,y,1):
                if s1[i]==s2[j]:
                    self.process(s1,s2,i+1,j+1,lcslen,"{}{}".format(curlcs,s1[i]),res,x,y)
                    break

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution()
		ans = ob.all_longest_common_subsequences(s, t)
		for i in ans:
			print(i, end = " ")
		print()




# } Driver Code Ends