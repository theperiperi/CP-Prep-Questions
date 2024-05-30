class Solution:
    def partitionString(self, s: str) -> int:
        temp = set()
        ans = 1
        for ch in s:
            if ch not in temp:
                temp.add(ch)
            else:
                ans += 1
                temp = set()
                temp.add(ch)

        return ans
