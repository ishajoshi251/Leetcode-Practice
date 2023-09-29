//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    long long int mod=1e9+7;
    public:
    //Function to count number of ways to reach the nth stair.
    int countWays(int n)
    {
        // your code here
        
        if (n <= 2)
        return n;

        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int c = (a%mod + b%mod)%mod;
            a = b;
            b = c;
        }
        return b%mod;
        }
};



//{ Driver Code Starts.
int main()
{
    //taking total testcases
    int t;
    cin >> t;
    while(t--)
    {
        //taking stair count
        int m;
        cin>>m;
        Solution ob;
        cout<<ob.countWays(m)<<endl; // Print the output from our pre computed array
    }
    return 0;
}

// } Driver Code Ends