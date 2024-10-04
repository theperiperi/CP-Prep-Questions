class Solution:
    memory={}
    def climbStairs(self, n: int) -> int:
        #for 0 or 1 stairs only one way possible
        if n==0 or n==1:
            return 1
        
        #for a new computation store in memory array
        if n not in self.memory:
            self.memory[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        
        #this runs only once,but takes last index from memory array and returns
        return self.memory[n]
       
   
