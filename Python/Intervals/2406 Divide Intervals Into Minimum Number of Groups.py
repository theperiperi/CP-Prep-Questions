class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_sorted=sorted(i[0] for i in intervals)
        end_sorted=sorted(i[1] for i in intervals)
        pointer=0
        num_groups=0

        for start in start_sorted:
            if start>end_sorted[pointer]:
                pointer+=1
            else:
                num_groups+=1
        return num_groups
