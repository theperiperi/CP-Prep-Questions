class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        
        def compare(self,red,blue,balls):
            number_of_balls=1
            while balls>=number_of_balls:
                balls-=number_of_balls
                
                if balls==blue-number_of_balls:
                    blue=balls
                    balls=red
                else:
                    red=balls
                    balls=blue
                
                number_of_balls+=1
            return number_of_balls-1

        return max(compare(self,red,blue,max(red,blue)),compare(self,red,blue,min(red,blue)))
