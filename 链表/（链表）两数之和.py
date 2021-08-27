# coding:utf-8
''''''
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)  # 建立一个空链表
        res = ans  # 保存头节点
        c = 0  # 进位，取0或1
        while l1 or l2:  # 一直到两个都结束为止
            a = l1.val
            b = l2.val
            ans.next = ListNode((a + b) % 10 + c)  # 正常计算流程相加
            ans = ans.next
            c = (a + b + c) // 10  # 整除，得到是否进位
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if c:  # 最后一位是否有进位
            ans.next = ListNode(1)
        return res.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode(1)  # 保留完整的链表
        l3 = a  # 保留完整的链表
        c = 0  # 进位
        while l1 or l2:
            x = l1.val if l1 else 0  # 没有下一节点时取0
            y = l2.val if l2 else 0
            tmp = x + y
            if tmp + c < 10:
                l3.next = ListNode(tmp + c)
                c = 0  # 不进位，清零
            else:
                l3.next = ListNode(tmp + c - 10)
                c = 1  # 进位，进1
            if l1:
                l1 = l1.next  # 进入链表的下一节点
            if l2:
                l2 = l2.next  # 进入链表的下一节点
            l3 = l3.next
        if c == 1:
            l3.next = ListNode(1)  # 最后一个进位增加一个末尾节点，元素为1
        return a.next  # a的第一个是0，因此去头节点

    def addTwoNumbers3(self,l1,l2):
        ans = ListNode(0)
        head = ans
        c = 0
        while l1 or l2:
            a = 0
            b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            ans_val = (a+b+c) % 10
            c = 1 if (a+b+c) > 9 else 0
            ans.next = ListNode(ans_val)
            ans = ans.next
        if c==1:
            ans.next = ListNode(1)
        return head.next