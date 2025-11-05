# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        if not root: return "[]"
        serial_arr=[]
        queue=deque([root]) if root else deque()
        
        while queue:
            node=queue.popleft()
            if node is None:
                serial_arr.append("null")
                continue
            if node.left:
                queue.append(node.left)
            else:
                queue.append(None)
            if node.right:
                queue.append(node.right)
            else:
                queue.append(None)
            serial_arr.append(str(node.val))
        
        return "[" + ",".join(serial_arr) + "]" 

    def deserialize(self, data):
        print(data)
        if len(data)==2: return None
        data=data[1:-1].split(",")
        root=TreeNode(int(data[0]))
        queue=deque([root])
        
        i=1
        while queue and i<len(data):
            node=queue.popleft()
            if i<len(data) and data[i]!="null":
                node.left=TreeNode(int(data[i]))
                queue.append(node.left)
            else:
                node.left=None
            i+=1
            if i<len(data) and data[i]!="null":
                node.right=TreeNode(int(data[i]))
                queue.append(node.right)
            else:
                node.right=None
            i+=1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))