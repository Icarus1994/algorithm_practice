# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        node1 = pHead1
        node2 = pHead2
        common = set()
        while node1 or node2:
            # print(node1.val, node2.val)
            if node1:
                length = len(common)
                common.add(node1.val)
                if len(common) == length:
                    return node1
                else:
                    node1 = node1.next
            if node2:
                length = len(common)
                common.add(node2.val)
                if len(common) == length:
                    return node2
                else:
                    node2 = node2.next
        return None

# 题目
# 输入两个链表，找出它们的第一个公共结点。

# 注意
# 公共节点并不是说这两个节点是同一个实例对象，只要求值（node.val)相同而已