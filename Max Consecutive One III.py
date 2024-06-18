class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_num=0
        max_zero=0

        l=0
        r=len(nums)

        for i in range(r):
            if nums[i]==0:
                max_zero+=1

            while max_zero > k:
                if nums[l]==0:
                    max_zero -=1
                l+=1

            w=i-l+1
            max_num = max(max_num,w) 
        return max_num 
