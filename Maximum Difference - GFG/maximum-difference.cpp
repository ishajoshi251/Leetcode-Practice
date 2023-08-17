//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
    public:
    /*You are required to complete this method */
    int findMaxDiff(int arr[], int n)
    {
      //Your code here
      int i;
      stack<int>left;
      vector<int>l(n,0);
      vector<int>r(n,0);
      stack<int>right;
      for(i=0;i<n;i++)
      {
          if(left.empty())
          {
              left.push(arr[i]);
          }
          else
          {
              while(!left.empty() && left.top() >= arr[i])
              {
                  left.pop();
              }
              if(left.empty())
              {
                  left.push(arr[i]);
              }
              else
              {
                  l[i] = left.top();
                  left.push(arr[i]);
              }
          }
      }
      for(i=n-1;i>=0;i--)
      {
          if(right.empty())
          {
              right.push(arr[i]);
          }
          else
          {
              while(!right.empty() && right.top() >= arr[i])
              {
                  right.pop();
              }
              if(right.empty())
              {
                  right.push(arr[i]);
              }
              else
              {
                  r[i] = right.top();
                  right.push(arr[i]);
              }
          }
      }
      int maxi = INT_MIN;
      for(i=0;i<n;i++)
      {
          maxi =  max(abs(l[i]-r[i]),maxi);
      }
      return maxi;
      
    }
};

//{ Driver Code Starts.
int main()
{
   int t;
   cin>>t;
   while(t--)
   {
   	int n;
   	cin>>n;
   	int a[n];
   	for(int i=0;i<n;i++)
   	cin>>a[i];
   	Solution ob;
   	cout<<ob.findMaxDiff(a,n)<<endl;
   }
    return 0;
}



// } Driver Code Ends