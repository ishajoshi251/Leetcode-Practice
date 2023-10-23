# ranges[i][0] is the start of ith range
# ranges[i][1] is the end of ith range

class Solution:
        
    def max_non_overlapping(self,ranges):
        # code here
        n = len(ranges)
        ranges.sort()
        start = ranges[0][0]
        end = ranges[0][1]
        ans = []
        for i in range(1,n):
            if end>ranges[i][0]:
                end = min(end,ranges[i][1])
            else:
                ans.append([start,end])
                start = ranges[i][0]
                end = ranges[i][1]
        ans.append([start,end])
        return len(ans)


#{ 
 # Driver Code Starts
# driver code
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        line = input().strip().split()
        ranges = [[]  for j in range(n)]
        j=0
        for i in range(0,2*n,2):
            ranges[j].append(int(line[i]))
            ranges[j].append(int(line[i+1]))
            j+=1
            
        obj=Solution()
        print( obj.max_non_overlapping(ranges) )
# } Driver Code Ends