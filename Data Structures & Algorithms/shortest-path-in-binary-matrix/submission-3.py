class Solution:

    def _feasibleDirection(self, grid: List[List[int]], i: int, j: int, direction: List[int], visit: Set) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        dr, dc = direction
        if (i + dr) < 0 or (i + dr) == ROWS or (j + dc) < 0 or (j + dc) == COLS or ((i + dr), (j + dc)) in visit or grid[(i + dr)][(j + dc)]:
            return False
        return True

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        visit = set()

        queue.append((0,0))
        visit.add((0,0))
        length = 1

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1],
                      [1, 1], [1, -1], [-1, 1], [-1, -1]]

        while queue:

            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == ROWS - 1 and j == COLS - 1:
                    return length

                for direction in directions:
                    if not self._feasibleDirection(grid, i, j, direction, visit):
                        continue

                    dr, dc = direction
                    visit.add((i + dr, j + dc))
                    queue.append((i + dr, j + dc))

            length += 1
        
        return -1
        