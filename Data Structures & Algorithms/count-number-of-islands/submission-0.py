from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_rows = len(grid)
        max_cols = len(grid[0])

        total_islands = 0
        visited_islands = set()

        def bfs(row, col):
            queue = deque()
            visited_islands.add((row, col))
            queue.append((row, col))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                row, col = queue.popleft()
                for row_dr, col_dr in directions:
                    r, c = row + row_dr, col + col_dr
                    if (
                        r in range(max_rows) and c in range(max_cols)
                        and (r, c) not in visited_islands
                        and grid[r][c] == "1"
                    ):
                        queue.append((r, c))
                        visited_islands.add((r, c))


        for row in range(max_rows):
            for col in range(max_cols):
                if (row, col) in visited_islands:
                    continue
                visited_islands.add((row, col))
                if grid[row][col] == "1":
                    bfs(row, col)
                    total_islands += 1
        
        return total_islands
