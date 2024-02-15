class Solution:
    memory={}
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        if n not in self.memory:
            self.memory[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.memory[n]
       
