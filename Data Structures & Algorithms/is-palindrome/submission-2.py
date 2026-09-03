class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:

            while not s[L].isalnum() and L < R:
                print("L")
                L += 1
                
            while not s[R].isalnum() and L < R:
                print("R")
                R -= 1

            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True