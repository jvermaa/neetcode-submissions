class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # this can hold the current minimum at the location.

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_at_this_index = min(self.min_stack[-1] if self.min_stack else val , val)

        self.min_stack.append(min_at_this_index)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
