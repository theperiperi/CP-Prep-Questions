class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        digit_to_letters={
            '2':'abc',"3":"def","4":"ghi","5":"jkl",
            "6":'mno',"7":'pqrs','8':'tuv','9':'wxyz'
        }

        def backtrack(current_combination,next_digit):
            if len(current_combination)==len(digits):
                results.append(''.join(current_combination))
                return
            
            current_digit=digits[next_digit]
            for letter in digit_to_letters[current_digit]:
                current_combination.append(letter)
                backtrack(current_combination,next_digit+1)
                current_combination.pop()

        results=[]
        backtrack([],0)
        return results
        
