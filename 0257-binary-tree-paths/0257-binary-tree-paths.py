# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        paths = []
        self.dfs(root, path, paths)
        return paths
    
    def dfs(self, root, path, paths):
        if not root:
            return 
        
        path.append(root.val)
        if root.left is None and root.right is None:
            str_path = "->".join(map(str, path))
            paths.append(str_path)
            path.pop()
            return
            
        self.dfs(root.left, path, paths)
        self.dfs(root.right, path, paths)
        path.pop()
        return
            