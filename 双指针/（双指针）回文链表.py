# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （双指针）回文链表
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/23 9:32
**************************************************
'''
'''
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        start,end = 0,len(l)-1
        while start < end:
            if l[start]!=l[end]:
                return False
            start+=1
            end-=1
        return True