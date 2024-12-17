import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count the frequency of each character and create a max-heap based on character value
        char_heap = [(-ord(char), count) for char, count in Counter(s).items()]
        heapq.heapify(char_heap)  # Convert list into a heap

        result = ""  # Result string to store the final output

        # Process characters from the heap
        while char_heap:
            # Get the character with the highest lexicographical order
            char_value, count = heapq.heappop(char_heap)
            
            # Add the character up to the repeatLimit times
            while count > repeatLimit and char_heap:
                result += chr(-char_value) * repeatLimit
                count -= repeatLimit
                
                # Get the next largest character and add it once
                next_char_value, next_count = heapq.heappop(char_heap)
                result += chr(-next_char_value)
                
                # Push the next character back into the heap if it still has remaining occurrences
                if next_count - 1 > 0:
                    heapq.heappush(char_heap, (next_char_value, next_count - 1))
            
            # Add the remaining occurrences of the character
            result += chr(-char_value) * count

        # Handle edge case where last characters are the same and exceed repeatLimit
        if result:
            last_char_index = len(result) - 1
            while last_char_index >= 0 and result[last_char_index] == result[-1]:
                last_char_index -= 1
            if len(result) - last_char_index - 1 > repeatLimit:
                result = result[:last_char_index + 1 + repeatLimit]

        return result
