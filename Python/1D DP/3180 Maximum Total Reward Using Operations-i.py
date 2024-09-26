class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        rewardValues.sort()
        possible=set()

        for r in rewardValues:
            dp=possible.copy()
            for val in possible:
                if val<r:
                    dp.add(val+r)
            dp.add(r)
            possible=dp
        return max(possible)
