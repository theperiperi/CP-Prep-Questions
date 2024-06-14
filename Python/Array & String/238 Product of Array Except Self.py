class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        prod1=1
        answer=[]
        case=1

        if nums.count(0)==1:
            case=2
            for i in nums:
                if i!=0:
                    prod1=prod1*i

        
        for i in nums:
            prod=prod*i

        
        for i in nums:
            #case 1: not 0
            if i!=0:
                answer.append(prod//i)

            #case 2: one 0
            elif case==2 and i==0:
                answer.append(prod1)


            #case 3: multiple 0
            else:
                answer.append(prod)
        return answer

        
