class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                #upper triang consideration
                for j in range(i,len(matrix)):
                    #swap upper and lower triangle
                    x=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=x
        
        def horizo_flip(matrix):
            for r in range(len(matrix)):
                left=0
                right=len(matrix)-1

                while left<right:
                    x=matrix[r][left]
                    matrix[r][left]=matrix[r][right]
                    matrix[r][right]=x
                    left+=1
                    right-=1
                    
        transpose(matrix)
        horizo_flip(matrix)
