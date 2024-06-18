class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        sum=0

        for i in range(len(nums)):
            if nums[i]==1:
                sum+=1
                maxi=max(maxi,sum)
            else:
                sum=0
        return maxi
