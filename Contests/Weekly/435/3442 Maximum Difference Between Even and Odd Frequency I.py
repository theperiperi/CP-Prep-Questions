class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        even = {k: v for k, v in counter.items() if v % 2 == 0}
        odd = {k: v for k, v in counter.items() if v % 2 != 0}

        return max((max(odd.values())-min(even.values())),(min(odd.values())-max(even.values())))
