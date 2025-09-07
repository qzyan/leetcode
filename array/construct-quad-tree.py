"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.helper(grid, 0, 0, n - 1, n - 1)

    def helper(self, grid, tlr, tlc, brr, brc):
        is_leaf = True
        val = grid[tlr][tlc]
        for row in range(tlr, brr + 1):
            for col in range(tlc, brc):
                if grid[row][col] != val:
                    is_leaf = False
        
        if is_leaf:
            return Node(val, is_leaf, None, None, None, None)
        
        mid_row = (tlr + brr) // 2
        mid_col = (tlc + brc) // 2
        tl = self.helper(grid, tlr, tlc, mid_row, mid_col)
        tr = self.helper(grid, tlr, mid_col + 1, mid_row, brc)
        bl = self.helper(grid, mid_row + 1, tlc, brr, mid_col)
        br = self.helper(grid, mid_row + 1, mid_col + 1, brr, brc)

        return Node(val, is_leaf, tl, tr, bl, br)

