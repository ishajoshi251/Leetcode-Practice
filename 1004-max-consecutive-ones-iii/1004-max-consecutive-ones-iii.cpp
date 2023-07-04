class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size();
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