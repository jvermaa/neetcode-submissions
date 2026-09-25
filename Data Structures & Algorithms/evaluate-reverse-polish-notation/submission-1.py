class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        shtack = []

        operands = {'+', '-', '*', '/'}

        for n in tokens:
            if n in operands:
                a = int(shtack.pop())
                b = int(shtack.pop())
                if n == '+':
                    shtack.append(b + a)
                
                elif n == "-":
                    shtack.append(b - a)
                
                elif n == '*':
                    shtack.append(b * a)
                
                elif n == '/':
                    shtack.append(b/a)
            else:
                shtack.append(n)
        
        return int(shtack[-1])