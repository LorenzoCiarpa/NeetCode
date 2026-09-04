# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:


    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorder = deque()

        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.inorder.append(curr.val)
                curr = curr.right
        

    def next(self) -> int:
        return self.inorder.popleft()

    def hasNext(self) -> bool:
        return len(self.inorder) > 0

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()