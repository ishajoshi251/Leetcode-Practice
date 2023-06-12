#User function Template for python3

# You are required to complete this fucntion
# Function should return an integer
class Solution:
    def findK(self, a, n, m, k):
        # Your code goes here
        r1 = 0
        r2 = n-1
        c1 = 0
        c2 = m-1
        direction = 0
        li = []
        while r1 <= r2 and c1 <= c2:
            if direction == 0:
                for i in range(c1,c2+1):
                    li.append(a[r1][i])
                r1 += 1
            elif direction == 1:
                for i in range(r1,r2+1):
                    li.append(a[i][c2])
                c2 -= 1
            elif direction == 2:
                for i in range(c2,c1-1,-1):
                    li.append(a[r2][i])
                r2 -= 1
            else:
                for i in range(r2,r1-1,-1):
                    li.append(a[i][c1])
                c1 += 1
            direction = (direction +1)%4    
        return li[k-1]



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        obj = Solution()
        print(obj.findK(matrix, n[0], n[1], n[2]))

# } Driver Code Ends