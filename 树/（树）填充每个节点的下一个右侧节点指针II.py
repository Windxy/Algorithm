# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （树）填充每个节点的下一个右侧节点指针II
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/28 9:19
**************************************************
'''
'''
给定一个二叉树
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        Queue = [root]
        while len(Queue)!=0:
            len_of_Queue = len(Queue)
            tmp = len_of_Queue
            for i in range(len_of_Queue):
                last = Queue.pop()
                tmp -= 1
                if tmp == 0:
                    last.next = None
                else:
                    last.next = Queue[-1]
                if last.left:
                    Queue.insert(0, last.left)
                if last.right:
                    Queue.insert(0, last.right)
        return root

    def connect2(self,root: 'Node') -> 'Node':
        # 不用额外空间的方法，思路也比较简单，迭代就行了
        if root==None:
            return root

        Head_left = root
        Head_left.next = None
        while Head_left:
            Head = Head_left

            while Head:
                if Head.left:
                    Head.left.next = Head.right
                else:
                    break

                if Head.next:
                    Head.right.next = Head.next.left
                else:
                    Head.right.next = None
                    break

                Head = Head.next

            Head_left = Head_left.left
        return root