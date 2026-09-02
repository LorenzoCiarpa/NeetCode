class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * capacity

    def hash(self, key: int) -> int:
        return key % self.capacity


    def insert(self, key: int, value: int) -> None:
        idx = self.hash(key)

        while self.map[idx] is not None:
            k, v = self.map[idx]
            # print(k, v, idx)

            if k == key:
                self.map[idx] = (key, value)
                
                return
            
            idx += 1
            idx = idx % self.capacity

        self.map[idx] = (key, value)
        self.size += 1

        if self.size >= self.capacity // 2:
            self.resize()

        return

    def get(self, key: int) -> int:
        idx = self.hash(key)

        while self.map[idx] is not None:

            k, v = self.map[idx]
            if k == key:
                return v
            
            idx += 1
            idx = idx % self.capacity

        return -1


    def remove(self, key: int) -> bool:
        idx = self.hash(key)

        while self.map[idx] is not None:
            k, v = self.map[idx]
            if k == key:
                self.map[idx] = None
                self.size -= 1
                return True
            
            idx += 1
            idx = idx % self.capacity

        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair[0], pair[1])
    

