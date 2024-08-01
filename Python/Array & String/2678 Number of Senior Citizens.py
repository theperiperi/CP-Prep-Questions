class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter=0
        for i in details:
            if int(i[11:13]) > 60:
                counter+=1
        return counter
