class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=c2=0
        e1 = -1111111
        e2 = -1111111
        ans = []
        for i in range(len(nums)):
            if c1 == 0 and e2 != nums[i]:
                c1 = 1
                e1 = nums[i]
            elif c2 == 0 and e1 != nums[i]:
                c2 = 1
                e2 = nums[i]
            elif e1 == nums[i]:
                c1 += 1
            elif e2 == nums[i]:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        a = len(nums)//3
        b=c= 0
        for i in range(len(nums)):
            if nums[i] == e1:
                b += 1
            if nums[i] == e2:
                c += 1
        if b>a:
            ans.append(e1)
        if c>a:
            ans.append(e2)
        return ans
                