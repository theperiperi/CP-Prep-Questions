class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        if 'IV' in s:
            result += 4
            s = s.replace('IV','')

        if 'IX' in s:
            result += 9
            s = s.replace('IX','')

        if 'XL' in s:
            result += 40
            s = s.replace('XL','')

        if 'XC' in s:
            result += 90
            s = s.replace('XC','')

        if 'CD' in s:
            result += 400
            s = s.replace('CD','')

        if 'CM' in s:
            result += 900
            s = s.replace('CM','')

        for i in s:
            print(i)
            if i == 'M':
                result += 1000
            elif i == 'D':
                result += 500
            elif i == 'C':
                result += 100
            elif i == 'L':
                result += 50
            elif i == 'X':
                result += 10
            elif i == 'V':
                result += 5
            elif i == 'I':
                result += 1
        return result
