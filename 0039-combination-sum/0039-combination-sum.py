class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        com = []
        self.gen(0,candidates,[],com,target)
        return com
    def gen(self, i:int,candidates: List[int],temp: List[int],com: List[int],target:int) -> List[List[int]]:
        if i == len(candidates):
            if target == 0:
                com.append(temp[:])
            return
        if target == 0:
            com.append(temp[:])
            return
        if candidates[i]<=target:
            temp.append(candidates[i])
            self.gen(i,candidates,temp,com,target-candidates[i])
            temp.pop()
        
        self.gen(i+1,candidates,temp,com,target)

