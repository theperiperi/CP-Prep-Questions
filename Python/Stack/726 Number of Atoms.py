class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(formula):
            stack = [collections.defaultdict(int)]
            i, n = 0, len(formula)
            
            while i < n:
                if formula[i] == '(':
                    stack.append(collections.defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[start:i] or 1)
                    top = stack.pop()
                    for elem, cnt in top.items():
                        stack[-1][elem] += cnt * multiplier
                else:
                    start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    elem = formula[start:i]
                    start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[start:i] or 1)
                    stack[-1][elem] += count
            
            return stack[0]
    
        element_counts = parse_formula(formula)
        sorted_elements = sorted(element_counts.items())
        result = []
        
        for elem, count in sorted_elements:
            result.append(elem)
            if count > 1:
                result.append(str(count))
        
        return ''.join(result)
