# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （链表）两两交换链表中的节点
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/26 11:09
**************************************************
'''
'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return first
