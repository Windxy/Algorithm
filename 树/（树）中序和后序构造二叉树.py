# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （树）中序和后序构造二叉树
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/25 15:06
**************************************************
'''
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map = {val:idx for idx,val in enumerate(inorder)}
        def helper(left,right):
            if left>right:
                return None
            val = postorder.pop()# 弹出后遍历最后一个元素做根元素
            root = TreeNode(val)

            index = map[val] # 中序遍历中间那个元素，
            root.right = helper(index+1,right)  # 右子树
            root.left = helper(left,index-1)    # 左子树
            return root
        return helper(0,len(postorder)-1)