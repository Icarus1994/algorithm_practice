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
# 思路
# 链表复制问题，要求新链表的节点是区别于原来节点的新的一段内存空间，但每个新节点指向的随机节点，继续指向原来的随机节点即可
# 碰到链表问题不要第一时间想到list,如本题中可以通过两个关键变量实现：
# 1是每次创建一个新节点与原节点对应；2是p指针指向当前新节点的前一节点，然后使用p.next将前一节点与当前新节点连接。初始p自行创建一个新节点即可。
