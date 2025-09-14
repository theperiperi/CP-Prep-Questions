class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
        exact = set(wordlist)

        case_map = {}
        for word in wordlist:
            low = word.lower()
            if low not in case_map:
                case_map[low] = word 

        vowel_map = {}
        for word in wordlist:
            mask = "".join('*' if char in "aeiou" else char for char in word.lower())
            if mask not in vowel_map:
                vowel_map[mask] = word
        
        ans = []
        for query in queries:
            mask = "".join('*' if c in "aeiou" else c for c in query.lower())  
            if query in exact:
                ans.append(query)
            elif query.lower() in case_map:
                ans.append(case_map[query.lower()])
            elif mask in vowel_map:
                ans.append(vowel_map[mask])
            else:
                ans.append("")
        return ans
