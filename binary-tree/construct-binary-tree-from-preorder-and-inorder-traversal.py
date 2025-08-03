# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        recorder = {"preorder_idx": 0}
        inorder_val_idx = {val: idx for idx, val in enumerate(inorder)}
        return self.build_tree_helper(preorder, recorder, inorder, 0, len(inorder) - 1, inorder_val_idx)

    def build_tree_helper(self, preorder, recorder, inorder, inorder_left, inorder_right, inorder_val_idx):
        if inorder_left > inorder_right:
            return

        preorder_idx = recorder["preorder_idx"]
        if preorder_idx >= len(preorder):
            return

        val = preorder[preorder_idx]
        node = TreeNode(val)

        recorder["preorder_idx"] += 1
        inorder_idx = inorder_val_idx[val]

        node.left = self.build_tree_helper(preorder, recorder, inorder, inorder_left, inorder_idx - 1, inorder_val_idx)
        node.right = self.build_tree_helper(preorder, recorder, inorder, inorder_idx + 1, inorder_right, inorder_val_idx)

        return node