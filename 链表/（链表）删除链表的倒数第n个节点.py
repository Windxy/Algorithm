# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （链表）删除链表的倒数第n个节点
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/23 13:43
**************************************************
'''
'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # A先走，B等A走了n步后再走
        if head.next == None and n==1:return []
        head2 = head
        head_ans = head2
        while(n):
            n-=1
            head = head.next
        while(head.next):
            head2 = head2.next
            head = head.next
        head2.next = head2.next.next
        return head_ans

s = Solution()
l = ListNode(1)
s.removeNthFromEnd(l,1)