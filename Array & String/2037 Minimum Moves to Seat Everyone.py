class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats=sorted(seats)
        students=sorted(students)
        return sum([abs(seats[i]-students[i]) for i in range(len(seats))])


        
