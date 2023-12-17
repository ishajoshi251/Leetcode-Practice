class Solution:
    def countTestedDevices(self, b: List[int]) -> int:
        devices = 0
        for i in range(len(b)):
            if b[i] > 0:
                devices += 1
                for j in range(i+1,len(b)):
                    b[j] = max(0,b[j]-1)
            else:
                continue
        return devices