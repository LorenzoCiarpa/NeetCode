# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p, path_q = [], []
        self.binary(root, p.val, path_p)
        self.binary(root, q.val, path_q)

        path_p = list(reversed(path_p))
        path_q = list(reversed(path_q))

        shortest = min(len(path_p), len(path_q))
        anchestor = None
        for i in range(shortest):
            if path_p[i].val == path_q[i].val:
                anchestor = path_p[i]
        return anchestor

    def binary(self, root, target, path):
        if not root:
            return False
        
        if root.val == target:
            path.append(root)
            return True
        
        if target < root.val:
            result = self.binary(root.left, target, path)
        else:
            result = self.binary(root.right, target, path)

        if result:
            path.append(root)
            return True
        
        return False