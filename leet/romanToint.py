class Solution(object):
    def romanToInt(self, s):
        roman_dict = {'M': 1000,'D': 500, 'C': 100, 'L': 50,'X': 10,'V': 5, 'I':1 }

        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += roman_dict[char]
        print(number)


Solution().romanToInt('III')
Solution().romanToInt('IV')
Solution().romanToInt('IX')
Solution().romanToInt('MCMIV')
Solution().romanToInt('LVIII')
Solution().romanToInt('MCMXCIV')