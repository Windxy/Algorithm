'''给定一个二叉树，判断它是否是高度平衡的二叉树。https://leetcode-cn.com/problems/balanced-binary-tree/'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 深度优先遍历
        # step1.确定退出状态,以及返回变量
        # step2.确定判断条件
        # step3.确定进入下一步
        def dfs(root):
            if root is None:
                return 0
            A = dfs(root.left)  # 到底为0
            B = dfs(root.right)
            if abs(A-B)>1 or A==-1 or B==-1:
                return -1   # 非平衡
            return max(A,B)+1   # 《二叉树的深度》，向上遍历一层

        return dfs(root)>-1
