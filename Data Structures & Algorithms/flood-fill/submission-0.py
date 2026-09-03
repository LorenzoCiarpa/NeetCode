class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if len(image) == 0:
            return image
        
        visit = set()
        original = image[sr][sc]
        
        self.floodAux(image, sr, sc, color, original, visit)
        return image

    def floodAux(self, image, r, c, color, original, visit):
        ROWS, COLS = len(image), len(image[0])
        if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit:
            return
        
        visit.add((r, c))
        
        if image[r][c] != original:
            return
        
        image[r][c] = color

        self.floodAux(image, r+1, c, color, original, visit)
        self.floodAux(image, r-1, c, color, original, visit)
        self.floodAux(image, r, c+1, color, original, visit)
        self.floodAux(image, r, c-1, color, original, visit)

        return
        