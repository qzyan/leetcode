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
        vals = []
        self.serialize_helper(root, vals)
        return ",".join(vals)

    def serialize_helper(self, root, vals):
        if not root:
            vals.append("N")
            return

        vals.append(str(root.val))
        self.serialize_helper(root.left, vals)
        self.serialize_helper(root.right, vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        recorder = {"curr_idx": 0}
        return self.deserialize_helper(data, recorder)

    def deserialize_helper(self, data, recorder):
        curr_idx = recorder["curr_idx"]
        val_str = data[curr_idx]
        recorder["curr_idx"] += 1
        if val_str == "N":
            return None
        
        root = TreeNode(int(val_str))
        root.left = self.deserialize_helper(data, recorder)
        root.right = self.deserialize_helper(data, recorder)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))