"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = set()
        p_ancestor = p
        while p_ancestor:
            p_ancestors.add(p_ancestor)
            p_ancestor = p_ancestor.parent
            
        q_ancestor = q
        while q_ancestor:
            if q_ancestor in p_ancestors:
                return q_ancestor
            q_ancestor = q_ancestor.parent