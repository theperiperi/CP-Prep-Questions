class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        n = len(intervals)
        new = []
    

        while i < n and intervals[i][1] < newInterval[0]:
            new.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        new.append(newInterval)

        # Add all intervals after the new interval
        while i < n:
            new.append(intervals[i])
            i += 1

        return new
