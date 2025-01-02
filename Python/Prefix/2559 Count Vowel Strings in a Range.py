class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels='aeiou'
        res=[]
        prefix=[0] * (len(words)+1)

        #init prefix sums
        for word_index in range(len(words)):
            prefix[word_index + 1] = prefix[word_index]
            if words[word_index][0] in vowels and words[word_index][-1] in vowels:
                prefix[word_index + 1] += 1

        #computing queries
        for query in queries:
            ans= prefix[query[-1] + 1] - prefix[query[0]]
            res.append(ans)
       
        return res
