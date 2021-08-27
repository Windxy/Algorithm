# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （链表）旋转链表
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/23 9:59
**************************************************
'''
'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        lens = 0
        tmp = head
        tmp2 = head
        while 1:
            if tmp.next:
                tmp = tmp.next
            else:
                break
            lens += 1
        tmp.next = tmp2

        index = lens - k % lens
        if index == lens:
            return head
        while index:
            tmp2 = tmp2.next
            index -= 1
        ans = tmp2.next
        tmp2.next = None

        return ans

class Solution2:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        oldTail = head
        length = 1
        while oldTail.next:     #计算长度
            length += 1
            oldTail = oldTail.next
        oldTail.next = head     #闭环

        newTail = head
        number = k % length     #求余数
        for _ in range(length - number - 1):    #找到新的尾结点
            newTail = newTail.next
        newHead = newTail.next

        newTail.next = None     #断链
        return newHead