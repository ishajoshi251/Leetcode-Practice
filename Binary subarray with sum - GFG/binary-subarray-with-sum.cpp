//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
  public:
    int numberOfSubarrays(vector<int>& arr, int N, int target){
        // code here
        int count = 0;
        int summ = 0;
        unordered_map<int,int>mp;
        int i;
        for(i=0;i<N;i++){
            summ += arr[i];
            if(summ == target){
                count++;
            }
            if(mp.find(summ-target) != mp.end()){
                count += mp[summ-target];
            }
            if(mp.find(summ) != mp.end()){
                mp[summ]++;
            }
            else{
                mp[summ] = 1;
            }
        }
        return count;
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin >> N;
        int target; 
        cin >> target;
        vector<int> arr(N);
        for(int i=0; i<N; i++)
            cin >> arr[i];
        Solution obj;
        cout<<obj.numberOfSubarrays(arr, N, target)<<endl;
    }
    return 0;
}
// } Driver Code Ends