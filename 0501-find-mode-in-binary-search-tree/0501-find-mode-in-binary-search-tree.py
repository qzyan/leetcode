# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        max_count = 0
        curr_count = 0
        prev_val = None
        vals = []
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()

            if prev_val == curr.val:
                curr_count += 1
            if prev_val != curr.val:
                curr_count = 1
            if curr_count == max_count:
                vals.append(curr.val)
            elif curr_count > max_count:
                vals = [curr.val]
                max_count = curr_count
            
            prev_val = curr.val
            if curr.right:
                curr = curr.right
            else:
                curr = None
                       
        return vals