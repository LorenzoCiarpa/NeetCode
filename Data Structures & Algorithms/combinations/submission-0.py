class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combos = []
        self.helper(n, 1, [], combos, k)
        return combos
        
    def helper(self, n: int, i: int, curCombo: List[int], combos: List[List[int]], k: int) -> None:
        if len(curCombo) == k:
            combos.append(curCombo.copy())
            return
        if i > n:
            return
        
        for j in range(i, n+1):
            curCombo.append(j)
            self.helper(n, j + 1, curCombo, combos, k)
            curCombo.pop()
        return
        