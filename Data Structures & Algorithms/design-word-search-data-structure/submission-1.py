class TrieNode:
    def __init__(self):
        self.children = {}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        return

    def search(self, word: str) -> bool:
        curr = self.root
        return self.searchAux(word, curr)
        
    
    def searchAux(self, word: str, root: Optional[TrieNode]) -> bool:
        curr = root
        i=None
        for i, c in enumerate(word):
            if c == ".":
                if i + 1 == len(word) and curr.children:
                    result = False
                    for char in curr.children:
                        result = curr.children[char].word
                    return result
                
                result = False
                for char in curr.children:
                    result = result or self.searchAux(word[i+1:], curr.children[char])
                return result

            if c not in curr.children:
                return False                
            curr = curr.children[c]

        if i + 1 == len(word) and curr.word:
            return True
        return False