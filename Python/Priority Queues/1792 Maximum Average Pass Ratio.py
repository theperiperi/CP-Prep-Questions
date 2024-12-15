class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        num_classes = len(classes)
        total_ratio = 0
        priority_queue = []
        
        # Initialize the heap with the decrease in benefit of adding one more student
x            total_ratio += passed / total
            delta_ratio = (passed - total) / (total * (total + 1))  # Change in ratio
            priority_queue.append((delta_ratio, passed, total))
        
        heapify(priority_queue)  # Build a min-heap based on delta_ratio
        
        # Add 'extraStudents' extra students to the most beneficial classes
        for _ in range(extraStudents):
            smallest_delta, passed, total = priority_queue[0]
            if smallest_delta == 0:
                break  # No further improvement possible
            total_ratio -= smallest_delta  # Adjust the total ratio
            new_delta = (passed - total) / ((total + 1) * (total + 2))  # New delta after adding a student
            heapreplace(priority_queue, (new_delta, passed + 1, total + 1))
        
        return total_ratio / num_classes
