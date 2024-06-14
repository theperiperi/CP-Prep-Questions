class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        rows=len(matrix)
        cols=len(matrix[0])

        start=0
        end=rows*cols-1

        while start<=end:
            mid=(start+end)//2
            mid_value=matrix[mid//cols][mid%cols]

            if mid_value==target:
                return True
            
            elif mid_value<target:
                start=mid+1
            else:
                end=mid-1
        return False
