class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots=set(dictionary)
        res=[]
        words=sentence.split()

        for word in words:
            for letter_index in range(len(word)+1):
                prefix=word[:letter_index]
                if prefix in roots:
                    res.append(prefix)
                    break
            else:
                res.append(word)
        return " ".join(res)
