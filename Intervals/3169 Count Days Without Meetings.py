class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        meetings.sort()

        merged_meetings=[]
        curr_start,curr_end=meetings[0]

        for start, end in meetings[1:]:
            if start<=curr_end+1:
                curr_end=max(curr_end,end)
            else:
                merged_meetings.append((curr_start,curr_end))
                curr_start=start
                curr_end=end
            
        merged_meetings.append((curr_start,curr_end))

        meeting_days=sum(end-start+1 for start,end in merged_meetings)
        return days-meeting_days
