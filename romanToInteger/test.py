class Solution(object):
    def romanToInt(self, s):
        roman = {"I": 1, 
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000
                 }
        total = 0
        
        for romawi in range(len(s)):
            if romawi + 1 < len(s) and roman[s[romawi]] < roman[s[romawi + 1]]:
                total -= roman[s[romawi]]
            else:
                total += roman[s[romawi]]
        return total
        
solution = Solution()
