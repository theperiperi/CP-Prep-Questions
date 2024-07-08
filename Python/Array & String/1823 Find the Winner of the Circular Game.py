class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n>1:
            return (self.findTheWinner(n-1, k)+(k-1))%n+1 
        return 1
