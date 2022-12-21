# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count_recorder = {
            "count": 0
        }
                
        return self.dfs(root, count_recorder, k)
    
    def dfs(self, root, count_recorder, k):
        if root is None:
            return
        
        left_rest = self.dfs(root.left, count_recorder, k)
        if left_rest is not None:
            return left_rest
        
        count_recorder["count"] += 1
        if count_recorder["count"] == k:
            return root.val
        
        right_rest = self.dfs(root.right, count_recorder, k)
        return right_rest