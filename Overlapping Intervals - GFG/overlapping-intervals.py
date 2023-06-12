class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		Intervals.sort()
		ans = []
		start = Intervals[0][0]
		end = Intervals[0][1]
		for i in range(1,len(Intervals)):
		    if end>= Intervals[i][0]:
		        end = max(end,Intervals[i][1])
            else:
                ans.append([start,end])
                start = Intervals[i][0]
                end = Intervals[i][1]
        ans.append([start,end])
        return ans
                
#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends