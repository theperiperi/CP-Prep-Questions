class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        merged=[intervals[0]]

        for interval in intervals:
            #no overlap
            if merged[-1][-1]<interval[0]:
                merged.append(interval)

            #if overlap, edit end limit
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged
