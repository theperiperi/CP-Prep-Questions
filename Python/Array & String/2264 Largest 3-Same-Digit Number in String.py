class Solution(object):
    def largestGoodInteger(self, num):
        for i in reversed(range(10)):
            substring = str(i)*3
            if substring in num:
                return substring
        return ""
