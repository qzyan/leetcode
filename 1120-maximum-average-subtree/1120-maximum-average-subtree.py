# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        _, _, max_avg = self.helper(root)
        return max_avg
    
    def helper(self, root):
        if not root:
            return 0, 0, 0
        
        left_avg, left_count, left_max_avg = self.helper(root.left)
        right_avg, right_count, right_max_avg = self.helper(root.right)
        
        total = left_avg * left_count + right_avg * right_count + root.val
        count = left_count + right_count + 1
        avg = total / count
        
        return avg, count, max(avg, left_max_avg, right_max_avg)
        