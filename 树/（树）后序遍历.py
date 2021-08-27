# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （树）后序遍历
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/29 18:36
**************************************************
'''
'''
给定一个二叉树，返回它的 后序 遍历。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]