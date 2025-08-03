# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        while queue:
            vals_in_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    vals_in_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    vals_in_level.append("N")

            if not self.is_symmetric(vals_in_level):
                return False
        
        return True

    def is_symmetric(self, vals):
        left, right = 0, len(vals) - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            
            left += 1
            right -= 1

        return True
                


