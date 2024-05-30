class Solution:
    def addDigits(self, num: int) -> int:
        return num if num < 10 else self.addDigits(sum(int(digit) for digit in str(num)))
