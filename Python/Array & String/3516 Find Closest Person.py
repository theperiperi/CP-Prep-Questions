class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        dist_x = abs(z-x)
        dist_y = abs(y-z)

        if dist_x == dist_y:
            return 0
        elif dist_x < dist_y:
            return 1
        else:
            return 2
