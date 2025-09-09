class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        people_per_day = [0] * (n + 1)
        people_per_day[1] = 1
        active_sharers = 0
        MOD = 10**9 + 7

        for day in range(2, n + 1):
            if day - delay > 0:
                active_sharers = (active_sharers + people_per_day[day - delay]) % MOD
            if day - forget > 0:
                active_sharers = (active_sharers - people_per_day[day - forget] + MOD) % MOD
            people_per_day[day] = active_sharers

        total_aware = 0
        for day in range(n - forget + 1, n + 1):
            total_aware = (total_aware + people_per_day[day]) % MOD

        return total_aware
