'''给定一个二叉树，找出其最大深度。https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode):
        # 深度优先遍历
        # step1.确定退出状态以及返回变量
        # step2.确定判断条件
        # step3.确定进入下一步
        def dfs(root):
            if root is None:
                return 0
            depth_L = dfs(root.left)
            depth_R = dfs(root.right)
            depth = max(depth_L,depth_R)+1
            return depth

        return dfs(root)
