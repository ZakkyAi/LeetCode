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

        #for romawi in s:
        #    total += roman[romawi]

        
        for i in range(len(s)):
            
            index1 = 0
            index2 = 1
            
            char_lis = [s[index1], s[index2]]
            index1 += 1
            index2 += 1
            
            print(f"debuG index1: {index1}")
            print(f"debuG index2: {index2}")
            print(f"debug LIST: {char_lis}")     
            print(i)
        
        
        
        
        if char_lis[0] > char_lis[1]:
            value_a = roman[char_lis[0]]
            value_b = roman[char_lis[1]]
            total = value_a + value_b
        else:
            value_a = roman[char_lis[0]]
            value_b = roman[char_lis[1]]
            result = value_a - value_b
            total = abs(result)
        print(f"{total}")
        return total

solution = Solution()
solution.romanToInt("IXIV")