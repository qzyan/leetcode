# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr = root
        low_bound = None
        high_bound = None
        
        while curr:
            if curr.val == target:
                return curr.val
            if curr.val > target:
                high_bound = curr.val
                curr = curr.left
            else:
                low_bound = curr.val
                curr = curr.right
                
        if low_bound is None:
            return high_bound
        if high_bound is None:
            return low_bound
        return low_bound if abs(low_bound - target) < abs(high_bound - target) else high_bound