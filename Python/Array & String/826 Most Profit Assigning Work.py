class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))  

        max_profit = 0
        best_profit = 0 
        i = 0

        for ability in sorted(worker):
            while i < len(jobs) and jobs[i][0] <= ability:  
                best_profit = max(best_profit, jobs[i][1]) 
                i += 1
            max_profit += best_profit

        return max_profit
