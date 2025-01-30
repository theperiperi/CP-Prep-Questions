class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        return n.count('1')
