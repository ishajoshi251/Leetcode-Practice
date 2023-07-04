class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int count=0;
        int ans=0;
        int i;
        unordered_map<int,int>mp;
        for(i=0;i<nums.size();i++){
           
            if(nums[i]%2 != 0){
                count++;
            }
            if(count == k){
                ans++;
            }
            if(mp.find(count-k) != mp.end()){
                ans += mp[count-k];
            }
            mp[count]++;
        }
        return ans;
    }
};