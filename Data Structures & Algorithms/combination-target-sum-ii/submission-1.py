class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        candidates = sorted(candidates)
        self.dfs(0, candidates, 0, [], combos, target)
        return combos
    
    def dfs(self, i, candidates, curSum, curCombo, combos, target):

        if curSum == target:
            combos.append(curCombo.copy())
            return

        if i >= len(candidates):
            return
        
        
        # i don't take item i
        j = i + 1
        while j < len(candidates) and candidates[j - 1] == candidates[j]:
            j += 1
        self.dfs(j, candidates, curSum, curCombo, combos, target)

        if candidates[i] + curSum > target:
            return
        
        curCombo.append(candidates[i])
        curSum += candidates[i]
        self.dfs(i + 1, candidates, curSum, curCombo, combos, target)
        
        elem = curCombo.pop()
        curSum -= elem

        return

        