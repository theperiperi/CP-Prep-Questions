class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def divide(a, b):
            return (int(a/b)) 
        def mult(a, b):
            return (a*b)
        def add(a, b):
            return (a+b)
        def sub(a, b):
            return (a-b)
        a = {
            '+' : add,
            '-' : sub,
            '*' : mult,
            '/' : divide
        }
        stack = []
        for i in tokens:
            if i in a:
                y = stack.pop()
                x = stack.pop()
                stack.append(a[i](x,y))
            else:
                stack.append(int(i))
        return stack.pop()
