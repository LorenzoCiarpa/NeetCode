class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""

        for s in strs:
            length = len(s)
            a += str(length) + "#" + s
        
        return a

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        # print(f"decoding: {s}")

        while i < len(s):

            number = ""
            while s[i] != "#":
                number += s[i]
                i+=1

            i += 1
            j = 0
            newS = ""
            # print(f"number: {number}")
            while j < int(number):
                newS += s[i + j]
                j += 1

            result.append(newS)
            i += j  
        return result          