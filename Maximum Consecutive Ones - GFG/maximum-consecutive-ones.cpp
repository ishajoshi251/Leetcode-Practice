//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int longestOnes(int n, vector<int>& nums, int k) {
        // Code here
        int i = 0;
        int j = 0;
        int len = 0;
        while(j<n){
            if(nums[j] == 1){
               j++;
            }
            else if(nums[j] == 0 && k>0){
                j++;
                k--;
                
            }
            else if(nums[i] == 1 && k<=0){
                i++;
            }
            else if(nums[i] == 0 && k<=0){
                k++;
                i++;
            }
            len = max(len,j-i);
            
        }
        return len;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> nums;
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            nums.push_back(x);
        }

        int k;
        cin >> k;

        Solution obj;
        cout << obj.longestOnes(n, nums, k) << endl;
    }
    return 0;
}
// } Driver Code Ends