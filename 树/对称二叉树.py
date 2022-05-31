'''给定一个二叉树，检查它是否是镜像对称的。https://leetcode-cn.com/problems/symmetric-tree/'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self,root:TreeNode):
        # 深度优先遍历
        # step1.确定退出状态以及返回变量
        # step2.确定判断条件
        # step3.确定进入下一步
        def dfs(left:TreeNode,right:TreeNode):
            if left is None and right is None:
                return True
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left) and left.val == right.val
        return dfs(root.left,root.right)
