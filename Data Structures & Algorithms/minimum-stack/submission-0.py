class MinStack:


    # we are going to have 2 stacks
    # First stack will be the main stack
    # the second stack will keep track of the minimum at each level
    # so lets say both stacks are currently empty
    # then I add a value.
    # in the first insertion, our top of the main stack and the minimum would be the same value

    # However, from the second insertion and so on, we will need to push the minimum between the two in the min stack
    # This would allow us to keep track of the minimum at a certain level of stack

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        min_at_this_level = min(val, self.min_stack[-1] if self.min_stack else val)

        self.min_stack.append(min_at_this_level)

    def pop(self) -> None:

        if self.main_stack:
            self.main_stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
