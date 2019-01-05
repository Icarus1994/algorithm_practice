# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        node1 = pHead1
        node2 = pHead2
        if node1.val <= node2.val:
            nNode = node1
            node1 = node1.next
        else:
            nNode = node2
            node2 = node2.next
        # 虽然在这里pHead就已经指向了刚初始化的nNode,
        # 但是之后会对nNode.next作修改，所以返回的pHead是正确的
        pHead = nNode
        while node2 or node1:
            if not node1:
                nNode.next = node2
                nNode = nNode.next
                node2 = node2.next
            elif not node2:
                nNode.next = node1
                nNode = nNode.next
                node1 = node1.next
            else:
                if node1.val <= node2.val:
                    nNode.next = node1
                    nNode = nNode.next
                    node1 = node1.next
                else:
                    nNode.next = node2
                    nNode = nNode.next
                    node2 = node2.next
        return pHead
# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

# 思路
# 每次node = node.next时相当于有一个指针，从node移向下一个Node
# 创建一个node，让node一直等于Node.next，等价于创建了一个新列表
# 始终要记得python的赋值是新增了对原来对象的引用，不是拷贝