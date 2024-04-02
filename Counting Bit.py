class Solution:
    def countBits(self, n: int) -> List[int]:
        
        power = 1
        ans = [0  for _ in range(n+1)] 

        for i in range(1,  n + 1):

            if power * 2 == i:
                power = i
        
            ans[i] = 1 + ans[i - power]
        return ans
