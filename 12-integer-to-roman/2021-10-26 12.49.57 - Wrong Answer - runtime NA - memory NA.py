class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        s = ""
        for i in reversed(roman_dict.keys()):
            tmp = num//i
            if tmp > 0:
                s += roman_dict[i]*tmp
                num = num%i
        return s
                
            