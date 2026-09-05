class Queue:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyStack:

    def __init__(self):
        self.stack = None
        self.size = 0
        

    def push(self, x: int) -> None:
        node = Queue(x)

        if self.size == 0:
            self.stack = node
        else:
            node.prev = self.stack
            self.stack.next = node
            self.stack = self.stack.next
        
        self.size += 1
        
        return

    def pop(self) -> int:
        if self.size == 0:
            return -1
        
        tmp = self.stack.val
        if self.size > 1:
            self.stack = self.stack.prev
            self.stack.next = None
        else:
            self.stack = None
        self.size -= 1
        return tmp

    def top(self) -> int:
        if self.size == 0:
            return -1
        return self.stack.val

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()