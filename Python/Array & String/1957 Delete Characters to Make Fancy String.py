class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = None
        count = 0

        ans = []
        for index in s:
            if index == prev:
                count += 1
            else:
                prev = index
                count = 1
            if count <= 2:
                ans.append(index)
        return "".join(ans)
