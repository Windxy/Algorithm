import queue
class TreeNode():
    def __init__(self,data):
        self.left = None
        self.right= None
        self.data = data

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

def preorder(node:TreeNode):
    if not isinstance(node,TreeNode) or node is None:
        return
    # 中左右 前序遍历
    # 左中右 中序遍历
    # 左右中 后序遍历
    print(node.data,end=' ')
    preorder(node.left)
    preorder(node.right)

# preorder(node1)

# 一层一层 层序遍历
def levelOrder(root):
    # write code here
    if not root:
        return []
    Q = [root]
    ans = []
    while len(Q):
        N = len(Q)
        temp_Q = []
        for i in range(N):
            temp = Q.pop(0)
            temp_Q.append(temp.data)
            if temp.left:
                Q.append(temp.left)
            if temp.right:
                Q.append(temp.right)
        ans.append(temp_Q)
    return ans
print(levelOrder(node1))