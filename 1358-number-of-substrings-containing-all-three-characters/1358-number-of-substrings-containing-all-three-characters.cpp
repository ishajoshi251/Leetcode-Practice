class Solution {
public:
    int numberOfSubstrings(string s) {
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