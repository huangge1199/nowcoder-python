#!/usr/bin/env python3
# @author 轩辕龙儿
# @date 2022/3/1
# @file reverseBetween.py

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
from common import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        pre = ListNode
        cur = head
        pre.next = cur
        for i in range(m - 1):
            pre = pre.next
            cur = cur.next
        for i in range(n - m):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        if m == 1:
            return pre.next
        else:
            return head
