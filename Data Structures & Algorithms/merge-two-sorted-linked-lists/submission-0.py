# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addNode(tail: Optional[ListNode], val: int):
    new_node = ListNode(val)
    tail.next = new_node
    tail = new_node
    return tail

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = tail = None

        if list1 and list2:

            if list1.val <= list2.val:
                head = tail = ListNode(list1.val)
                list1 = list1.next
            else:
                head = tail = ListNode(list2.val)
                list2 = list2.next
            
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    tail = addNode(tail, list1.val)
                    list1 = list1.next
                else:
                    tail = addNode(tail, list2.val) 
                    list2 = list2.next
            
            if list1 is None:
                tail.next = list2
            else:
                tail.next = list1

            return head
        
        if list1 is None:
            return list2
        else:
            return list1


            


            