class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        sack = []

        for i in tokens:
            if i in {"+", "-", "/", "*"}:
                a = int(sack.pop())
                b = int(sack.pop())
                # b-a

                if i == "+":
                    sack.append(b + a)
                elif i == "-":
                    sack.append(b-a)
                elif i == "*":
                    sack.append(b * a)
                elif i == "/":
                    sack.append(int(float(b)/a))
            
            else:
                sack.append(int(i))
        
        return int(sack[0])