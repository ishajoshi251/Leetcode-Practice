class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        #[20,0,18,11,0,0,0,0,0,0,17,28,0,11,10,0,0,15,29] 159
        #[16,9,25,16,1,9,20,28,8,0,1,0,1,27] 161 163
         #nums1 = [3,2,0,1,0], nums2 = [6,5,0] [2,0,2,0], nums2 = [1,4] [0,7,28,17,18] =71[1,2,6,26,1,0,27,3,0,30]=96
        a = sum(nums1)
        b = sum(nums2)
        a_count = 0
        b_count = 0
        ans = -1
        for i in range(len(nums1)):
            if nums1[i] == 0:
                a_count += 1
        for i in range(len(nums2)):
            if nums2[i] == 0:
                b_count += 1
        if (a>b and b_count == 0) or (b>a and a_count == 0):
            return ans
        elif a_count == 0 and a>b:
            diff = a-b
            while b_count and diff:
                b_count -= 1
                diff -= 1
            if b_count>0:
                return ans
            else:
                ans = a
        elif b_count == 0 and b>a:
            diff = b-a
            while a_count and diff:
                a_count -= 1
                diff -= 1
            if a_count>0:
                return ans
            else:
                ans = b
        elif a == b:
            if (a_count == 0 and b_count !=0) or(b_count == 0 and a_count != 0):
                return -1
            if a_count>b_count:
                while a_count:
                    a_count -= 1
                    a += 1
                ans = a
                
            else:
                while b_count:
                    b_count -= 1
                    b += 1
                ans = b
         
        else:
            if a>b:
                i = a_count
                while i:
                    a += 1
                    i -= 1
                diff = a-b
                if diff<b_count:
                    i = b_count
                    while i:
                        b += 1
                        i -= 1
                    ans = b
                else:
                    ans = a
            else:
                i = b_count
                while i:
                    b += 1
                    i -= 1
                diff = b-a
                if diff<a_count:
                    i = a_count
                    while i:
                        a += 1
                        i -= 1
                    ans = a
                else:
                    ans = b
        return ans
                
        
            

            