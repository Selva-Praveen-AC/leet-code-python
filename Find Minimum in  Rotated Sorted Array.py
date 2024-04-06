#approach 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

#approach 2
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        return nums[0]

#approach 3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]
            
