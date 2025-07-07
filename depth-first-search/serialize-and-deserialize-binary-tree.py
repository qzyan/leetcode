# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        vals = []
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node is None:
                    vals.append("N")
                else:
                    vals.append(str(curr_node.val))
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)

        return " ".join(vals)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(" ")
        root = TreeNode(int(data[0]))
        idx = 1
        queue = collections.deque([root])
        while queue:
            curr_node = queue.popleft()

            val_str1 = data[idx]
            val_str2 = data[idx + 1]
            idx += 2
            node1 = None if val_str1 == "N" else TreeNode(int(val_str1))
            node2 = None if val_str2 == "N" else TreeNode(int(val_str2))

            curr_node.left = node1
            curr_node.right = node2
            if node1:
                queue.append(node1)
            if node2:
                queue.append(node2)

        return root

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))