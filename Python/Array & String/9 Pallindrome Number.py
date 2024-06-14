class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        return y == y[::-1]
