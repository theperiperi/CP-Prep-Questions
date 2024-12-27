class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        res=0
        val=values[0]

        for i in range(1,n):
            res=max(res, val+(values[i]-i))
            if (values[i]+i) > val:
                val=values[i]+i
        return res
