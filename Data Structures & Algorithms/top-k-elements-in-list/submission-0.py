class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        maxHeap = []
        result = []

        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        
        for key in frequency:
            heapq.heappush(maxHeap, (-1 * frequency[key], key))
        
        for i in range(k):
            elem = heapq.heappop(maxHeap)
            result.append(elem[1])
        
        return result