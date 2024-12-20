class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        max_time = events[0][1]
        max_button = events[0][0]
        for event_index in range(len(events)-1):
            duration = events[event_index+1][1] - events[event_index][1]
            if duration > max_time:
                max_time = duration
                max_button = events[event_index+1][0]
            if duration == max_time:
                max_button=min(max_button,events[event_index+1][0])
        return max_button
            
