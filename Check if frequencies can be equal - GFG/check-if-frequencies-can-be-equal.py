#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        r=[]
        for i in s:
            r.append(i)
        l=list(set(r))
        l1=[]
        for i in range(len(l)):
            l1.append(r.count(l[i]))
        l1.sort()
        if(len(set(l1))==1):
            return True
        m=-1
        n=l1[0]
        l1[0]=l1[0]-1
        if(l1[0]==0):
            m=l1.pop(0)
        if(len(set(l1))==1):
            return True
        if(m==-1):
            l1[0]=n
        else:
            l1.insert(0,n)
        l1[-1]=l1[-1]-1
        if(len(set(l1))==1):
            return True
        else:
            return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends