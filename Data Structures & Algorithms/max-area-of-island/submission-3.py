from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_rows = len(grid)
        max_cols = len(grid[0])

        visited_islands = set[tuple]()
        max_size_of_island = 0

        def bfs(row, col):
            queue = deque()
            visited_islands.add((row, col))
            queue.append((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            island_size = 1

            while queue:
                row, col = queue.popleft()
                for row_dr, col_dr in directions:
                    target_row = row + row_dr
                    target_col = col + col_dr
                    if (
                        target_row in range(max_rows)
                        and target_col in range(max_cols)
                        and (target_row, target_col) not in visited_islands
                        and grid[target_row][target_col] == 1
                    ):
                        island_size += 1
                        queue.append((target_row, target_col))
                        visited_islands.add((target_row, target_col))
            
            return island_size


        for row in range(max_rows):
            for col in range(max_cols):
                if (row, col) not in visited_islands and grid[row][col] == 1:
                    island_size = bfs(row, col)
                    max_size_of_island = max(max_size_of_island, island_size)
        
        return max_size_of_island
