class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        prev_sum = 0

        for i in range(1, n + 1):
            if i % 10 == 0:
                prev_sum = sum(int(d) for d in str(i))
            else:
                prev_sum += 1
            groups[prev_sum] += 1

        max_size = max(groups.values())
        return sum(1 for count in groups.values() if count == max_size)
