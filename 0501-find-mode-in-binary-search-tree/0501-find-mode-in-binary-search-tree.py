# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        recorder = {
            "max_count": 0,
            "curr_count": 0,
            "prev_val": None
        }
        
        vals = []
        self.inorder_traverse(root, recorder, vals)
        return vals
        
    def inorder_traverse(self, root, recorder, vals):
        if root is None:
            return 
        
        self.inorder_traverse(root.left, recorder, vals)
        
        if recorder["prev_val"] == root.val:
            recorder["curr_count"] += 1
        else:
            recorder["curr_count"] = 1
            
        if recorder["curr_count"] == recorder["max_count"]:
            vals.append(root.val)
        elif recorder["curr_count"] > recorder["max_count"]:
            vals.clear()
            vals.append(root.val)
            recorder["max_count"] = recorder["curr_count"]
        
        recorder["prev_val"] = root.val
        
        self.inorder_traverse(root.right, recorder, vals)
        return            
        
            