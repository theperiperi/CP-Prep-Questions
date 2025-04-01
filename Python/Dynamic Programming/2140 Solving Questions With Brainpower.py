class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        dp[n-1] = questions[n-1][0]

        for index in range(n-2, -1, -1):
            points, brain = questions[index]

            next_index = min(index + brain + 1, n)

            total = points + (dp[next_index] if next_index < n else 0)

            skip_points = dp[index + 1]
            dp[index] = max(total, skip_points)

        return dp[0]
