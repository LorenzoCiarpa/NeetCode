class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combo = []
        for i in range(len(position)):
            combo.append((position[i], speed[i]))
        
        combo = sorted(combo, reverse=True)
        prev = combo[0]
        total = 1
        for i in range(1, len(combo)):
            x0, v0 = prev[0], prev[1]
            x1, v1 = combo[i][0], combo[i][1]

            if x1 < x0 and v1 == v0:
                prev = combo[i]
                total += 1
                continue
                
            t = (x0 - x1) / (v1 - v0)
            if t < 0:
                total += 1
                prev = combo[i]
                continue
            
            if x0 + v0*t > target:

                total += 1
                prev = combo[i]
                continue

            
        return total
