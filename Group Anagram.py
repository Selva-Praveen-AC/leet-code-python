from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map=defaultdict(list)
        result=[]

        for s in strs:
            sorted_s=tuple(sorted(s))
            map[sorted_s].append(s)
        for i in map.values():
            result.append(i)

        return result
        
