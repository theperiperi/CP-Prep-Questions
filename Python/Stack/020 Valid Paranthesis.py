class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        mapping={"(" : ")",
        "[":"]",
        "{":"}"}

        for i in s:
           
            if stk==[]:
                if i in mapping.keys():
                    stk.append(i)
                else:
                    return False
            elif stk[-1] in mapping.keys():
                if i==mapping[stk[-1]]:
                    stk.pop()
                elif i in mapping.keys():
                    stk.append(i)
                else:
                    return False
                
        return stk==[]
            
            


                



             
        
