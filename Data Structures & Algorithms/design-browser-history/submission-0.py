class Node:
    def __init__(self, url=None, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

def printList(head):
    while head:
        print(head.url, end=" ")
        head = head.next
    print()


class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = Node(homepage)
        self.head = self.stack
        self.total_size = 0
        self.index = 0

    def visit(self, url: str) -> None:
        self.stack.next = Node(url, None, self.stack)
        self.stack = self.stack.next
        self.index += 1
        self.total_size = self.index
        # printList(self.head)

    def back(self, steps: int) -> str:
        curr = self.stack
        while self.index > 0 and steps > 0:
            self.stack = self.stack.prev
            self.index -= 1
            steps -= 1
        # printList(self.head)
        
        return self.stack.url

    def forward(self, steps: int) -> str:
        curr = self.stack
        while self.index < self.total_size and steps > 0:
            self.stack = self.stack.next
            self.index += 1
            steps -= 1
        # printList(self.head)
        
        return self.stack.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)