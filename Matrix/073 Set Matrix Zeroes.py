class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def zero_list(matrix):
            rows=set()
            columns=set()
            for row in range(len(matrix)):
                for column in range(len(matrix[0])):
                    if matrix[row][column]==0:
                        rows.add(row)
                        columns.add(column)
            return rows,columns


        def set_zeros(matrix,rows,columns):
            for row in rows:
                for ele in range(len(matrix[0])):
                    matrix[row][ele]=0
            for column in columns:
                for ele in range(len(matrix)):
                    matrix[ele][column]=0


        rows,columns=zero_list(matrix)
        set_zeros(matrix,rows,columns)
        
