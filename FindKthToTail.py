# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         # next的数据类型也是listNode
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0 :
            return None
        node = head
        list = []
        while node != None:
            list.append(node)
            node = node.next
        if k>len(list):
            return None
        else:
            return list[-k]

# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。