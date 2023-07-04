//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
    // 0 0 0  1 2 2 2 2
  public:
    int totalFruits(int N, vector<int> &fruits) {
        unordered_map<int,int>mp;
        int count = 0;
        int i=0;
        int j=0;
        while(j<N){
            mp[fruits[j]]++;
            if(mp.size() <= 2){
                count = max(count,j-i+1);
            }
            else if(mp.size()>2){
                mp[fruits[i]]--;
                if(mp[fruits[i]] == 0){
                    mp.erase(fruits[i]);
                }
                i++;
            }
            j++;
            
            
        }
        return count;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        vector<int> fruits(N);
        for (int i = 0; i < N; i++) cin >> fruits[i];
        Solution obj;
        cout << obj.totalFruits(N, fruits) << endl;
    }
    return 0;
}

// } Driver Code Ends