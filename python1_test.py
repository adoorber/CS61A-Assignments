# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        print ("[" + ",".join(res) + "]")
        return "[" + ",".join(res) + "]"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        # 处理字符串，分割出节点值列表
        vals = data[1:-1].split(",")
        index = 0
        root = TreeNode(int(vals[index]))
        index += 1
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # 处理左子节点
            if vals[index] != "null":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            # 处理右子节点
            if vals[index] != "null":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))