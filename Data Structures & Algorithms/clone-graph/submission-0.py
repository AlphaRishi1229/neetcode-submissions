"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new_map = {}

        def dfs(node: 'Node'):
            if node in old_to_new_map:
                return old_to_new_map[node]
            
            copy_node = Node(node.val)
            old_to_new_map[node] = copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            return copy_node
        
        return dfs(node) if node else None
