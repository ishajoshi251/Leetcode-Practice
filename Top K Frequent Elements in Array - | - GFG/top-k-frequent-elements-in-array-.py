import heapq
class Solution:
	def topK(self, nums, k):
		#Code here
		'''
		heap = []
		d = {}
		for i in nums:
		    if i in d:
		        d[i] += 1
		    else:
		        d[i] = 1
		for i in range(len(nums)):
		   
		     heapq.heappush(heap,[-d[nums[i]],-nums[i]])
		ans = []
		tmp = a=j = 0
	    for i in range(len(nums)):
	        tmp,a = heapq.heappop(heap)
	        if -a not in ans:
	            ans.append(-a)
	            j += 1
	            if j == k:
	                break
	        
		
		return ans
		'''
		n = len(nums)
        mp = {}
        pq = []

        for i in range(n):
            if nums[i] in mp:
		        mp[nums[i]] += 1
		    else:
		        mp[nums[i]] = 1

        for x in mp.items():
            heapq.heappush(pq,(-x[1], -x[0]))

        
        #print(pq)
        v = []
        while k > 0:
            v.append(-heapq.heappop(pq)[1])
            k -= 1

        return v

#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends