//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int countSubstring(string s) {
        // Code here
        int count= 0;
        int a = -1;
        int b = -1;
        int c = -1;
        int i;
        for(i=0;i<s.size();i++){
            if(s[i] == 'a'){
                a = i;
            }
            else if(s[i] == 'b'){
                b = i;
            } 
            else if(s[i] == 'c'){
                c = i;
            }
            if(i>=2){
                count += min(a,min(b,c))+1;
            }
            
        }
        return count;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;

        Solution obj;
        cout << obj.countSubstring(s) << endl;
    }
    return 0;
}
// } Driver Code Ends