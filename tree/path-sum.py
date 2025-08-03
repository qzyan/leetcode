# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum, 0)

    def dfs(self, node, targetSum, curr_sum):
        if node is None:
            return False
        
        curr_sum += node.val
        if not node.left and not node.right:
            return curr_sum == targetSum

        if self.dfs(node.left, targetSum, curr_sum):
            return True
        
        return self.dfs(node.right, targetSum, curr_sum)