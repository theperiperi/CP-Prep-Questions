from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        row, col = rStart, cStart
        direction_row, direction_col = 0, 1  # Initial direction is to the right
        spiral_turns = 2
        result = []
        steps = 1
        next_steps = 2

        while len(result) < (rows * cols):
            if 0 <= row < rows and 0 <= col < cols:
                result.append([row, col])
            
            row += direction_row
            col += direction_col
            steps -= 1

            if steps == 0:
                direction_row, direction_col = direction_col, -direction_row
                spiral_turns -= 1

                if spiral_turns == 0:
                    spiral_turns = 2
                    steps = next_steps
                    next_steps += 1
                else:
                    steps = next_steps - 1
        
        return result
