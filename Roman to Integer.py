class Solution:
    def romanToInt(self, S):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev = 0
        
        for c in reversed(S):
            value = roman_map[c]
            if value < prev:
                total -= value
            else:
                total += value
                prev = value 
                
        return total  
