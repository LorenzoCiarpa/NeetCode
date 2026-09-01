class TreeNode:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        
        curr = self.root
        while curr:
            if key == curr.key:
                curr.val = val
                return

            elif key < curr.key:
                if not curr.left:
                    curr.left = TreeNode(key, val)
                    return
                else:
                    curr = curr.left
            
            else: # key > curr.key
                if not curr.right:
                    curr.right = TreeNode(key, val)
                    return
                else:
                    curr = curr.right
        self.inorderPrint(self.root)
        return
            

    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if key == curr.key:
                return curr.val
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val
    
    def getMinKey(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.key
    
    def getMinsFromNode(self, root) -> Tuple[int, int]:
        if not root:
            return -1

        curr = root
        while curr.left:
            curr = curr.left
        return curr.key, curr.val

        
    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:
        self.root = self.removeAux(self.root, key)

    def removeAux(self, root, key) -> None:
        if root is None:
            return None

        if key > root.key:
            root.right = self.removeAux(root.right, key)
        elif key < root.key:
            root.left = self.removeAux(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if root.left and not root.right:
                return root.left
            if not root.left and root.right:
                return root.right
            
            
            minKey, minVal = self.getMinsFromNode(root.right)

            root.key = minKey
            root.val = minVal

            root.right = self.removeAux(root.right, minKey)

        return root        
        
        

    def getInorderKeys(self) -> List[int]:
        arr = []
        self.getInorderKeyAux(self.root, arr)
        return arr

    def getInorderKeyAux(self, root, arr) -> None:
        if not root:
            return
        
        self.getInorderKeyAux(root.left, arr)
        arr.append(root.key)
        self.getInorderKeyAux(root.right, arr)
        return

    def inorderPrint(self, root) -> None:
        if not self.root:
            return
        
        self.inorderPrint(root.left)
        print(f"{root.key}: {root.val}", end = " ")

