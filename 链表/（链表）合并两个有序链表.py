# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （链表）合并两个有序链表
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/25 15:32
**************************************************
'''
'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        L = ListNode(-1)
        L_h = L
        while l1 and l2:
            if l1.val <= l2.val:
                L.next = ListNode(l1.val)
                l1=l1.next
            else:
                L.next = ListNode(l2.val)
                l2 = l2.next
            L = L.next
        L.next = l1 if l1 is not None else l2
        return L_h.next