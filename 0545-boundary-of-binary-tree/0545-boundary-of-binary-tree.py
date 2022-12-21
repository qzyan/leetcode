# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        
        left_bound = self.find_left_bound(root)
        leaves = self.find_leaves(root)
        right_bound = self.find_right_bound(root)
        return [root.val] + left_bound + leaves + right_bound
    
    def find_left_bound(self, root):
        if not root.left:
            return []
        
        curr = root.left
        nodes = []
        while curr.left or curr.right:
            nodes.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        
        return nodes
    
    def find_leaves(self, root):
        stack = [root]
        leaves = []
        while stack:
            curr = stack.pop()
            if curr.left is None and curr.right is None:
                leaves.append(curr.val)
                continue
                
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        
        return leaves
    
    def find_right_bound(self, root):
        if not root.right:
            return []
        
        curr = root.right
        nodes = []
        while curr.left or curr.right:
            nodes.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
                
        nodes.reverse()
        return nodes
                