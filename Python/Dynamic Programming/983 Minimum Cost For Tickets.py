class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        dp = [0] * n
        
        left_week = 0
        left_month = 0

        for right in range(n):
            while days[right] -  days[left_week] >= 7:
                left_week += 1
            while days[right] - days[left_month] >=30:
                left_month += 1

            cost_day = (dp[right-1] if right>0 else 0) + costs[0]
            cost_week = (dp[left_week - 1] if left_week > 0 else 0) + costs[1]
            cost_month = (dp[left_month - 1] if left_month > 0 else 0) +costs[2]

            dp[right] = min(cost_day, cost_week, cost_month)
        return dp[n-1]
