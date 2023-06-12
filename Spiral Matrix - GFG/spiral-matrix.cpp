//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

	public:
	int findK(vector<vector<int>> &matrix, int n, int m, int k)
    {
        // Your code goes here
        
        int i,j;
        vector<int>v;
        int right = m-1;
        int top = 0;
        int left = 0;
        int bottom = n-1;
        
        while(top <= bottom && left <= right)
        {
            
            for(i=left;i<=right;i++)
            {
                v.push_back(matrix[top][i]);
                k--;
                if(k==0)
                {
                    return matrix[top][i];
                }
                
            }
            top++;
            for(i=top;i<=bottom;i++)
            {
                v.push_back(matrix[i][right]);
                k--;
                if(k==0)
                {
                    return matrix[i][right];
                }
                
            }
            right--;
            
            if(bottom >= top)
            {
                for(i=right;i>=left;i--)
                {
                    v.push_back(matrix[bottom][i]);
                    k--;
                    if(k==0)
                {
                    return matrix[bottom][i];
                }
                
                }
                bottom--;
            }
            
            if(left <= right)
            {
                for(i=bottom;i>=top;i--)
                {
                    v.push_back(matrix[i][left]);
                    k--;
                    if(k==0)
                {
                    return matrix[i][left];
                }
                
                }
              left++;
            }
            
        }
        return -1;
    }
};

//{ Driver Code Starts.

int main()
{
    int T;
    cin>>T;
  
    while(T--)
    {
        int n,m;
        int k=0;
        //cin>>k;
        cin>>n>>m>>k;
        vector<vector<int>> a(n, vector<int>(m, 0));
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>a[i][j];
            }
        }

        Solution obj;

        cout<< obj.findK(a, n, m, k) << "\n";
        
       
    }
}
// } Driver Code Ends