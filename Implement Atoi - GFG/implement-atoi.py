#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        
        if string[0] == '-':
            for i in range(1,len(string)):
                if 48<=ord(string[i])<=57:
                    continue
                else:
                    return -1
        
        else:
            for i in range(len(string)):
                if 48<=ord(string[i])<=57:
                    continue
                else:
                    return -1
        return int(string)
                

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends