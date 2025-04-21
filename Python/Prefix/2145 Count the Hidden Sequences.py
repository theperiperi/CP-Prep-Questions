class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        a = maxima = minima = 0
        for difference in differences:
            a+=difference
            maxima = max(maxima,a)
            minima = min(minima,a)
        return max(0,(upper-lower)-(maxima-minima)+1)
