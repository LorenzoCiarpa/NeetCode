class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [0]
        for elem in nums:
            self.push(elem)
        while len(self.heap) - 1 > self.k:
            self.pop()
        return

    def add(self, val: int) -> int:
        
        self.push(val)
        while len(self.heap) - 1 > self.k:
            self.pop()
        return self.heap[1]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i//2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp
            i = i // 2 

        return
    
    def pop(self):
        self.heap[1] = self.heap.pop()
        i = 1

        while (i * 2) < len(self.heap):

            if (i * 2) + 1 < len(self.heap) and self.heap[(i * 2) + 1] < self.heap[(i * 2)] and self.heap[i] > self.heap[(i * 2) + 1]:
                tmp = self.heap[(i * 2) + 1]
                self.heap[(i * 2) + 1] = self.heap[i]
                self.heap[i] = tmp
                i = (i * 2) + 1
            elif self.heap[i] > self.heap[i * 2]:
                tmp = self.heap[i * 2]
                self.heap[i * 2] = self.heap[i]
                self.heap[i] = tmp
                i = i * 2
            else:
                break

        return

    
        
