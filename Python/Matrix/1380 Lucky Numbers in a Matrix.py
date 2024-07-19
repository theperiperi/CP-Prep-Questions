class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        def findMinColumn(row):
            return min(range(len(matrix[row])), key=lambda j: matrix[row][j])
        
        def isMaxInColumn(val, col):
            return all(matrix[i][col] <= val for i in range(len(matrix)))
        
        for i in range(len(matrix)):
            minCol = findMinColumn(i)
            candidate = matrix[i][minCol]
            
            if isMaxInColumn(candidate, minCol):
                result.append(candidate)
        
        return result
