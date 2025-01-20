class Solution:
    def firstCompleteIndex(self, arr: list[int], matrix: list[list[int]]) -> int:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        painted_cells_in_row = [0] * num_rows
        painted_cells_in_col = [0] * num_cols
        value_to_row_map = [0] * (num_rows * num_cols + 1)
        value_to_col_map = [0] * (num_rows * num_cols + 1)

        for row_index, row in enumerate(matrix):
            for col_index, value in enumerate(row):
                value_to_row_map[value] = row_index
                value_to_col_map[value] = col_index

        for index, value in enumerate(arr):
            row_index = value_to_row_map[value]
            col_index = value_to_col_map[value]
            
            painted_cells_in_row[row_index] += 1
            if painted_cells_in_row[row_index] == num_cols:
                return index
            
            painted_cells_in_col[col_index] += 1
            if painted_cells_in_col[col_index] == num_rows:
                return index
        
        return -1
