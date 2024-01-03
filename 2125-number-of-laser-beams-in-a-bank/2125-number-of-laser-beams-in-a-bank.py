class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        v = []
        
        for i in range(len(bank)):
            x = bank[i]
            count = 0
            for j in range(len(x)):
                if x[j] == '1':
                    count += 1
            #print(count)
            if count == 0:
                continue
            v.append(count)
            
        if len(v) == 0 or len(v) == 1:
            return 0
        
        for i in range(len(v)-1):
            ans += v[i]*v[i+1]
        #ans += v[-2]*v[-1]
        return ans