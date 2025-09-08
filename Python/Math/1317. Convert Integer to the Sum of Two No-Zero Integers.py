class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def checkNoZero(num):
            while num > 0:
                remain = num % 10
                if remain == 0:
                    return False
                # chop off last digit
                num = num // 10
            return True
        a = 1
        b = n -1
        while not checkNoZero(a) or not checkNoZero(b):
            a += 1
            b -= 1
        return [a, b]
