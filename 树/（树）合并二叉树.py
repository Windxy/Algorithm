# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 合并二叉树
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/23 13:30
**************************************************
'''
'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def helper(t1,t2):
            if t1 is None:
                return t2
            if t2 is None:
                return t1
            root = TreeNode(t1.val+t2.val)
            root.left = helper(t1.left,t2.left)
            root.right = helper(t1.right, t2.right)
            return root