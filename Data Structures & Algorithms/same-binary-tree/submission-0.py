# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque()
        queue2 = deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 and queue2:
            tree1 = queue1.popleft()
            tree2 = queue2.popleft()


            if (tree1 and not tree2) or (not tree1 and tree2): 
                return False
            if tree1 and tree2 and tree1.val != tree2.val:
                return False
            
            if tree1:     
                queue1.append(tree1.left)
                queue1.append(tree1.right)

            if tree2:
                queue2.append(tree2.left)
                queue2.append(tree2.right)
        
        if len(queue1) != len(queue2):
            return False
        return True
