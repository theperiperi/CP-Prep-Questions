class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in range(1,61):
            x = num1 - num2 * k
            if x < k:
                return -1
            if bin(x).count("1") <= k:
                return k
        return -1
