class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, elem in enumerate(temperatures):
            while stack and elem > stack[-1][1]:
                
                popped = stack.pop()
                days = i - popped[0]
                result[popped[0]] = days

            stack.append((i, elem))
        
        return result
        