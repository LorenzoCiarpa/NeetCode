# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []

        n = 0
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
            n += 1
        
        mid = n // 2
        curr = head
        maxSum = 0
        for _ in range(mid):
            currSum = curr.val + stack.pop().val
            maxSum = max(currSum, maxSum)
            curr = curr.next
        
        return maxSum