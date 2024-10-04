class Solution(object):
    def multiply(self,num1, num2) :
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Determine lengths of num1 and num2
        m, n = len(num1), len(num2)
        
        # Initialize result array to store digits of the product
        result = [0] * (m + n)
        
        # Multiply each digit of num2 with each digit of num1
        for i in range(n-1, -1, -1):  # Iterate backwards through num2
            for j in range(m-1, -1, -1):  # Iterate backwards through num1
                # Calculate product and add to appropriate position in result array
                product = int(num1[j]) * int(num2[i])
                pos1, pos2 = i + j, i + j + 1
                total = product + result[pos2]
                result[pos1] += total // 10
                result[pos2] = total % 10
        
        # Convert result array to string format
        result_str = ''.join(map(str, result))
        
        # Remove leading zeros
        if result_str[0] == '0':
            result_str = result_str.lstrip('0')
        
        return result_str 
