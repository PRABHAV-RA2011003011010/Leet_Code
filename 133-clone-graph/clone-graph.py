"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        clone={}
        def dfs(node):

            if node in clone:
                return clone[node]
            new_node=Node()
            new_node.val=node.val
            clone[node]=new_node

            for neigh in node.neighbors:
                new_node.neighbors.append(dfs(neigh))

            return new_node
        return dfs(node) if node else node
        