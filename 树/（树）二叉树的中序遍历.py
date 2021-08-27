# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 二叉树的中序遍历
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/14 16:24
**************************************************
'''
# Definition for a binary tree node.
'''左中右'''
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)    #左中右，其他同理