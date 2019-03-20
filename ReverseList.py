# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:return pHead
        pre = None
        cur = pHead
        while cur:
            print("test cur:",cur.val)
            tmp =cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
