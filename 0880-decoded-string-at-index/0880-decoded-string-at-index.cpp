class Solution {
public:
    string decodeAtIndex(string s, int k) {
        int n = s.size();
        stack<long long>st;
        int i;
        st.push(0);
        long long int curr = 0;
        for(i=0;i<n;i++)
        {
            if(isdigit(s[i]))
            {
                long long int len = st.top() * (s[i] - '0');
                st.push(len);
                curr = len;
            }
             else
            {
                curr++;
                st.push(curr);
            }
        }
        
        int len = st.size();
        while(!st.empty())
        {
            k = k% st.top();
            len--;
            st.pop();
           if(k == 0 && isalpha(s[len-1]))
           {
               string x = "";
               x += s[len-1];
               return x;
           }
        }
         return "";
    }
    
};