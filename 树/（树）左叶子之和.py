# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （树）左叶子之和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/19 9:04
**************************************************
'''

'''
计算给定二叉树的所有左叶子之和。
示例：
    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 左叶子：没有子节点 + 其是根节点的左节点
# 遍历一棵树的节点，如果它的左节点是根节点
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0

        def checkIsNone(root):
            return 1 if root.left==None and root.right == None else 0

        def helper(root,ans):
            if root.left:
                ans += root.left.val if checkIsNone(root.left) else helper(root.left,ans)#是则返回，否则继续遍历
            if root.right and checkIsNone(root.right) != 1: #有右节点且不为空
                ans += helper(root.right)
            return ans
        return helper(root,ans) if root is not None else 0

s = Solution()

