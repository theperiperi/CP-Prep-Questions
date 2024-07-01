class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = len(s)
        one_num = 0
        for c in s:
            if c == '1':
                one_num += 1
        zero_num = l - one_num
        if one_num == 0:
            return s
        
        return "1" * (one_num - 1) + "0" * zero_num + "1"
      
