class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l=[]
        for i in nums:
            l.extend(i)
        s=[]
        k=len(nums)
        for i in l:
            if l.count(i)==k:
                s.append(i)
        s=list(set(s))
        s.sort()
        return s


        
