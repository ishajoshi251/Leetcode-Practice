#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        
        ans = []
        i = 0
        j = 0
        while i<n and j<m:
            if a[i] < b[j]:
                if len(ans) == 0 or ans[-1]!=a[i]:
                    ans.append(a[i])
                    i += 1
            elif a[i]>b[j]:
                if len(ans) == 0 or ans[-1]!=b[j]:
                    ans.append(b[j])
                    j += 1
            elif a[i] == b[j]:
                if len(ans) == 0 or ans[-1]!=a[i]:
                    ans.append(a[i])
                    i += 1
                    j += 1
                
        
        while i<n:
            if len(ans) == 0 or ans[-1]!=a[i]:
                ans.append(a[i])
                i += 1
    
        while j<m:
            if len(ans) == 0 or ans[-1]!=b[j]:
                ans.append(b[j])
                j += 1
        return ans
        '''
        
        i = 0
        j = 0
        v = []
        while i < n and j < m:
            if arr1[i] == arr2[j]:
                if len(v) == 0 or v[-1] != arr1[i]:
                    v.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                if len(v) == 0 or v[-1] != arr1[i]:
                    v.append(arr1[i])
                i += 1
            else:
                if len(v) == 0 or v[-1] != arr2[j]:
                    v.append(arr2[j])
                j += 1

        while i < n:
            if len(v) == 0 or v[-1] != arr1[i]:
                v.append(arr1[i])
            i += 1

        while j < m:
            if len(v) == 0 or v[-1] != arr2[j]:
                v.append(arr2[j])
            j += 1

        return v

                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends