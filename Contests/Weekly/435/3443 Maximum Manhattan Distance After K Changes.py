class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dirs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        x, y = 0, 0
        prev, cur, diff = 0, 0, 0
        total, best = 0, 0
        for c in s:
            x += dirs[c][0]
            y += dirs[c][1]
            cur = abs(x) + abs(y)
            diff = cur - prev
            prev = cur

            if diff == -1 and k > 0:
                diff = 1
                k -= 1
            total += diff
            if total > best:
                best = total

        return best
