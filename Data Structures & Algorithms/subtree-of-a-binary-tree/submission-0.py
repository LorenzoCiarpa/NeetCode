# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()
            if not curr:
                continue
            
            result = self.isSameTree(curr, subRoot)
            if result:
                return True
            
            queue.append(curr.left)
            queue.append(curr.right)

        return False
            

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))