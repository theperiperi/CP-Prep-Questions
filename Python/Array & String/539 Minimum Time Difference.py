class Solution(object):
    def findMinDifference(self, timePoints):
        # Convert times to minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
        
        # Sort times in ascending order
        minutes.sort()
        
        # Find minimum difference across adjacent elements
        min_diff = float('inf')
        for i in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[i + 1] - minutes[i])
        
        # Consider the circular difference between last and first element
        min_diff = min(min_diff, 24 * 60 - minutes[-1] + minutes[0])
        
        return min_diff
