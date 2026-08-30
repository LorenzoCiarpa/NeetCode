class MinStack:

    def __init__(self):
        self.stack = []
        self.aux_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = val if not self.aux_stack else min(self.aux_stack[-1], val)
        self.aux_stack.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.aux_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.aux_stack[-1]
        
        
