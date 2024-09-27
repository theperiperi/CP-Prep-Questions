class MyCalendarTwo:
    def __init__(self):
        self.booked_intervals = []
        
    def book(self, start: int, end: int) -> bool:
        for existing_start, existing_end in self.booked_intervals:
            if start < existing_end and end > existing_start:
                overlap_start = max(existing_start, start)
                overlap_end = min(existing_end, end)
                
                if self.has_double_booking(overlap_start, overlap_end):  # More descriptive
                    return False

        self.booked_intervals.append((start, end))
        return True
    
    def has_double_booking(self, start: int, end: int) -> bool:
        overlap_count = 0
        
        for existing_start, existing_end in self.booked_intervals:
            if start < existing_end and end > existing_start:
                overlap_count += 1
                if overlap_count == 2:
                    return True
        
        return False
