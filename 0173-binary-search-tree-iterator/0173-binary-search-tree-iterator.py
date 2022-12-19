# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # record the path to the curr node
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        curr = self.stack[-1]
        if not curr.right:
            node = self.stack.pop()
            while self.stack and self.stack[-1].right == node:
                node = self.stack.pop()
        else:
            node = curr.right
            while node:
                self.stack.append(node)
                node = node.left
        
        return curr.val
                   
        
        
        
        

    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()