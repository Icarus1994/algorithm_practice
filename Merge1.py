# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1: return pHead2
        if not pHead2: return pHead1

        # 因为下面的循环是先从判断node1是否小于等于node2的值，如果相等node1作为指针继续往前走
        # 所以当pHead1.val <= pHead2.val
        pHead = pHead1 if pHead1.val <= pHead2.val else pHead2
        node1 = pHead1
        node2 = pHead2
        fg = False
        while 1:
            while node1 and node1.val <= node2.val:
                if not node1.next:
                    node1.next = node2
                    fg = True
                    break
                elif node1.next.val <= node2.val:
                    node1 = node1.next
                else:
                    tmp = node1.next
                    node1.next = node2
                    node1 = tmp
                    break
            if fg: break
            while node2 and node2.val <= node1.val:
                if not node2.next:
                    node2.next = node1
                    fg = True
                    break
                elif node2.next.val <= node1.val:
                    node2 = node2.next
                else:
                    tmp = node2.next
                    node2.next = node1
                    node2 = tmp
                    break
            if fg: break
        return pHead

# 思路
# 在链表1，2上设置两指针，当两指针同时不为空时执行循环，比较指针指向节点大小
# 当一指针下一节点是空节点时，就将该节点的下一节点指向另一指针