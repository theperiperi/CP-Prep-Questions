class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        res = 2
        for p1 in points:
            counter = defaultdict(int)
            for p2 in points:
                if p1 != p2:
                    x1, y1 = p1
                    x2, y2 = p2
                    if x1 == x2:
                        counter["inf"] += 1
                    else:
                        counter[(y2 - y1) / (x2 - x1)] += 1
            res = max(res, max(counter.values()) + 1)
        return res
