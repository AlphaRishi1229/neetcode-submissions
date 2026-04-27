from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_nodes = set()
        atlantic_nodes = set()

        # dfs logic
        def dfs(row, col, visited_nodes, last_height):
            if (
                (row, col) in visited_nodes
                or row < 0 or col < 0 or row == rows or col == cols
                or heights[row][col] < last_height
            ):
                return
            
            visited_nodes.add((row, col))
            dfs(row+1, col, visited_nodes, heights[row][col])
            dfs(row-1, col, visited_nodes, heights[row][col])
            dfs(row, col+1, visited_nodes, heights[row][col])
            dfs(row, col-1, visited_nodes, heights[row][col])

        # add all pacific and atlantic nodes
        for row in range(rows):
            dfs(row, 0, pacific_nodes, heights[row][0])
            dfs(row, cols-1, atlantic_nodes, heights[row][cols-1])
        for col in range(cols):
            dfs(0, col, pacific_nodes, heights[0][col])
            dfs(rows-1, col, atlantic_nodes, heights[rows-1][col])

        mixed_set = pacific_nodes.intersection(atlantic_nodes)
        return list(mixed_set)
