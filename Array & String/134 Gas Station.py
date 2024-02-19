class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        #to check whether circle completion true
        if sum(gas)<sum(cost):
            return -1
        

        tank=ids=0

        for i in range(len(gas)):
            tank+=gas[i]-cost[i]
            if tank<0:
                tank=0
                ids=i+1
        return ids
        
