class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        left_idx, right_idx = 0, 0

        i = 0

        # odd
        for i in range(len(s)):
            curLength = 0
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:

                    if l == r:
                        curLength += 1
                    else:
                        curLength += 2

                    if curLength > length:
                        length = curLength
                        left_idx = l
                        right_idx = r

                    l -= 1
                    r += 1
                else:
                    break

            

        #even
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                continue

            curLength = 2
            l, r = i - 2, i + 1

            if curLength > length:
                length = curLength
                left_idx, right_idx = i - 1, i
                

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curLength += 2
                
                    if curLength > length:
                        length = curLength
                        left_idx, right_idx = l, r
                    
                    l -= 1
                    r += 1
                else: 
                    break
        
        return s[left_idx : right_idx + 1]