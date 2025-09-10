class Solution(object):
    def minimumTeachings(self, n, languages, friendships):

        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        
        # Convert user languages to sets for O(1) lookup
        user_langs = [set(l) for l in languages]

        # Step 1: Identify users who can't communicate with at least one friend
        need_help = set()
        for u, v in friendships:
            u -= 1  # Adjust to 0-based indexing
            v -= 1
            if user_langs[u].isdisjoint(user_langs[v]):
                need_help.add(u)
                need_help.add(v)

        # If all friends can communicate, no teaching is needed
        if not need_help:
            return 0

        # Step 2: Count how many affected users know each language
        lang_count = [0] * (n + 1)  # List indexed by language (1 to n)
        for user in need_help:
            for lang in user_langs[user]:
                lang_count[lang] += 1

        # Step 3: Find the language known by the most affected users
        max_known = max(lang_count)

        # Step 4: Calculate how many need to be taught this language
        return len(need_help) - max_known
