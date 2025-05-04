class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        mapping = [0] * 100
        count = 0
        for one, two in dominoes:
            key = one*10 + two if one<=two else two*10 + one
            count+=mapping[key]
            mapping[key]+=1
        return count
