# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:return
        p = RandomListNode(0)
        new_head = p
        old_node = pHead
        while old_node:
            new_node = RandomListNode(old_node.label)
            new_node.random = old_node.random
            p.next = new_node
            p = new_node
            old_node = old_node.next
        return new_head.next
