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
        count_map = {}
        max_count = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count_map[curr.val] = count_map.get(curr.val, 0) + 1
            max_count = max(count_map[curr.val], max_count)
            
            if curr.right:
                curr = curr.right
            else:
                curr = None
        
        vals = []
        for val, count in count_map.items():
            if count == max_count:
                vals.append(val)
                
        return vals