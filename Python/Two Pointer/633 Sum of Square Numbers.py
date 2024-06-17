class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        first = 0
        last = int(c ** 0.5)

        while first <= last: 
            total = first ** 2 + last ** 2
            if total == c:
                return True
            elif total > c:
                last -= 1
            else: 
                first += 1
        return False
