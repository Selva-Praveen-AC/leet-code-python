class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1):
            if s.lower()[i]!=s.lower()[i+1]:
                count+=1
        return count
