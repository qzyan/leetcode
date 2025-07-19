# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        recorder = {"result": -float("inf")}
        self.helper(root, recorder)
        return recorder["result"]

    # return is_bst, sum of bst, max, min
    def helper(self, root, recorder):
        if not root:
            recorder["result"] = max(recorder["result"], 0)
            return True, 0, -float('inf'), float('inf')
        
        is_left_bst, left_res, left_max, left_min = self.helper(root.left, recorder)
        is_right_bst, right_res, right_max, right_min = self.helper(root.right, recorder)

        is_bst = (left_max < root.val and root.val < right_min and is_left_bst and is_right_bst)
        if not is_bst:
            return False, float('inf'), float('inf'), float('inf')

        max_val = max(right_max, root.val)
        min_val = min(left_min, root.val)
        recorder["result"] = max(recorder["result"], left_res + right_res + root.val)
        return True, left_res + right_res + root.val, max_val, min_val

        