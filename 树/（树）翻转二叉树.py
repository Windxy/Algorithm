# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （树）翻转二叉树
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/16 8:28
**************************************************
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归
        if root == None:
            return
        # 1.取到左右节点
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # 2.根节点的左右节点进行交换
        root.right = left
        root.left = right
        # 3.返回根节点
        return root
