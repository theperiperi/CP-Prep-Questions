class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_points = [[x[0], x[2]] for x in rectangles]
        y_points = [[x[1], x[3]] for x in rectangles]
        x_points.sort(key=lambda x: x[0])
        y_points.sort(key=lambda x: x[0])
        
        def cut(points):
            iter_index = 0
            length = len(points)
            while iter_index < length - 1:
                if points[iter_index][1] > points[iter_index + 1][0]:
                    points[iter_index][1] = max(points[iter_index][1], points[iter_index + 1][1])
                    points.pop(iter_index + 1)
                    length -= 1
                else:
                    iter_index += 1
            
            return length >= 3
        
        x_cut = cut(x_points)
        y_cut = cut(y_points)
        
        return x_cut or y_cut
