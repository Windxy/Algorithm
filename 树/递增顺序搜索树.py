# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # new_list = []

        # def pre_order(root:TreeNode):
        #     if not isinstance(root,TreeNode) or not root:
        #         return
        #     pre_order(root.left)
        #     new_list.append(root.val)
        #     pre_order(root.right)

        # pre_order(root)

        # new_tree = TreeNode(new_list[0])
        # ans = new_tree
        # for i in range(1,len(new_list)):
        #     temp_tree = TreeNode(new_list[i])
        #     new_tree.right = temp_tree
        #     new_tree = new_tree.right

        # return ans
        new_list = []

        dummy = TreeNode(0)
        p = dummy

        def pre_order(root: TreeNode):
            nonlocal dummy
            if not isinstance(root, TreeNode) or not root:
                return
            pre_order(root.left)
            temp_tree = TreeNode(root.val)
            dummy.right = temp_tree
            dummy = dummy.right
            pre_order(root.right)

        pre_order(root)

        return p