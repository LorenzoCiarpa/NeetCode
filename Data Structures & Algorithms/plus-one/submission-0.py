class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        result = digits[i] + 1

        while result > 9 and i > 0:
            result -= 10
            digits[i] = result

            i -= 1
            result = digits[i] + 1
        
        if result < 10:
            digits[i] = result
            return digits
        
        result -= 10
        digits[i] = result

        digits.insert(0, 1)

        return digits

