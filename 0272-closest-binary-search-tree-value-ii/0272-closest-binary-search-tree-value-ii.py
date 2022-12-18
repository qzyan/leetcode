# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        inorder_vals = self.inorder_traversal(root)
        # find the index of the first val that is >= target
        idx = self.binary_search(inorder_vals, target)

        k_closest = self.find_k_closest(inorder_vals, idx, k, target)
        return k_closest
    
    def inorder_traversal(self, root):
        vals = []
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            vals.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = None
                
        return vals
    
    # return the index of the first val that is >= target
    def binary_search(self, vals, target):
        left, right = 0, len(vals) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if vals[mid] >= target:
                right = mid
            else:
                left = mid
                
        if vals[left] >= target:
            return left
        if vals[right] >= target:
            return right
        return len(vals)
    
    def find_k_closest(self, vals, idx, k, target):
        if idx == 0:
            return vals[:k]
        if idx == len(vals):
            return vals[-k:]
        
        left, right = idx - 1, idx
        k_closest = []
        while len(k_closest) < k and left >= 0 and right < len(vals):
            left_dist = target - vals[left]
            right_dist = vals[right] - target
            
            if left_dist <= right_dist:
                k_closest.append(vals[left])
                left -= 1
            else:
                k_closest.append(vals[right])
                right += 1
                
        while len(k_closest) < k and left >= 0:
            k_closest.append(vals[left])
            left -= 1
        while len(k_closest) < k and right < len(vals):
            k_closest.append(vals[right])
            right += 1
            
        return k_closest
        
        