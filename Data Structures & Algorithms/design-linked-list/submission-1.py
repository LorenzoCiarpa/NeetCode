class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(node):
    head = node
    while head is not None:
        print(head.val, sep=" ")
        head = head.next
    print()

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        i=0
        curr = self.head
        while i < index:
            curr = curr.next
            i += 1
        # printList(self.head)
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        self.size += 1
        # printList(self.head)
        return
        

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = Node(val)
        self.size += 1
        # printList(self.head)

        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return 
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        curr = self.head
        i = 0
        while i < index - 1:
            curr = curr.next
            i += 1

        node = Node(val, curr.next)
        curr.next = node
        self.size += 1
        # printList(self.head)

        return


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        tmp = None
        
        if index == 0:
            tmp = self.head
            self.head = self.head.next
        else:
            i = 0
            curr = self.head
            while i < index - 1:
                curr = curr.next
                i += 1
            tmp = curr.next    
            curr.next = curr.next.next

        del tmp
        # printList(self.head)
        self.size -= 1

        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)