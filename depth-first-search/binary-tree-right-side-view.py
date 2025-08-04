# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        if root is None:
            return results
        queue = collections.deque([root])
        while queue:
            for idx in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node.right:
                    queue.append(curr_node.right)
                if curr_node.left:
                    queue.append(curr_node.left)

                if idx == 0:
                    results.append(curr_node.val)

        return results