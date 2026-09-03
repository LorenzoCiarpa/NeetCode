class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        longest = 0
        L = 0

        for R in range(len(s)):
            if s[R] in window:
                til = window[s[R]]
                while L <= til:
                    window.pop(s[L])
                    L += 1
            
            window[s[R]] = R

            longest = max(longest, R - L + 1)
            # print(f"window: {window}")
        return longest
