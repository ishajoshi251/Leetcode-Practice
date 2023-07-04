class Solution {
public:
    int lengthOfLongestSubstring(string S) {
       unordered_map<char,int>mp;
        int i = 0;
        int j = 0;
        int len = 0;
        while(j<S.size()){
            mp[S[j]]++;
            if(mp[S[j]]>1){
                while(mp[S[j]]>1){
                    mp[S[i]]--;
                    if(mp[S[i]] == 0){
                        mp.erase(S[i]);
                    }
                    i++;
                    
                }
                
            }
            len = max(len,j-i+1);
            j++;
            
        }
        return len; 
    }
};