# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return None
        
        high = float("inf")
        low = -float("inf")
        while root:
            if root.val == target:
                return root.val
            if root.val > target:
                high = root.val
                root = root.left
            elif root.val < target:
                low = root.val
                root = root.right

                
        return high if high - target < target - low else low