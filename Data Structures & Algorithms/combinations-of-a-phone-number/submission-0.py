enum = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wyxz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combos = []
        self.helper(0, digits, "", combos)
        return combos

    def helper(self, i, digits, curCombo, combos):
        if len(curCombo) == len(digits):
            combos.append(curCombo)
            return

        if i >= len(digits):
            return

        chars = enum[digits[i]]

        for j in range(len(chars)):
            curCombo += chars[j]
            self.helper(i + 1, digits, curCombo, combos)
            curCombo = curCombo[:-1]
        
        return