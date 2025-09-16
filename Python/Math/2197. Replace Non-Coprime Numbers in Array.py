class Solution(object):
    def replaceNonCoprimes(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        stack = []
        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = stack.pop() * num // g
            stack.append(num)
        return stack
