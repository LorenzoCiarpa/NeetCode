class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        history = {}
        result = []

        for word in strs:
            arr = [0]*26
            for char in word:
                arr[ord(char) - 97] += 1
            if tuple(arr) in history:
                history[tuple(arr)].append(word)
            else:
                history[tuple(arr)] = [word]
        
        for key in history:
            result.append(history[key])

        return result