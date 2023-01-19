import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append(root)
        min_depth = 1
        
        while queue:
            size = len(queue)
            found_leaf_node = False
            for _ in range(size):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                if not curr_node.left and not curr_node.right:
                    found_leaf_node = True
                    break
            else:
                min_depth += 1
                
            if found_leaf_node:
                break
        
        return min_depth