class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        if n==1 and k==1:
            return True

        for start in range(n - k + 1):
            substring = s[start:start + k]

            # Check if all characters in the substring are the same
            if substring == s[start] * k:
                # Check boundary conditions
                if (start == 0 or s[start - 1] != s[start]) and (start + k == n or s[start + k] != s[start]):
                    return True

        return False
