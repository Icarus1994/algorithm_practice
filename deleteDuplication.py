# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def __init__(self):
        self.last = ListNode(0)
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        old = self.last
        node = pHead
        while node and node.next:
            if node.val == node.next.val:
                val = node.val
                while node and node.val == val:
                    node = node.next
            else:
                self.last.next = node
                self.last = node
                node = node.next
        if not node:
            self.last.next = None
        else:
            self.last.next = node
        return old.next
pHead = ListNode(1)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
pHead.next = node1
node1.next = node2
node2.next = node3
res = Solution().deleteDuplication(pHead)
print(res,node2)

# 思路
# 全局self.last指针，指向最后留下的节点，并将这些节点的next指向最后会得到的链表中的下一节点；
# node指针用来遍历链表
# 当node和node.next不同，且node.next与它下一个节点不同时才让self.last的下一节点指向node.next
# 在代码中实现上一条注释中的这个条件：代码中第二个while循环语句break后的node是第一个与之前val值不同的节点，
# 然后代码继续进入新的第一个while循环，重新判断node与node.next是否值相等

# 代码优化
# 参考牛客讨论区中的一个python解法

# 之前的错误思路
# 之前判断是否留下某个节点时，只是单纯地判断该节点是否与下一节点相等；
# 而且忽略了当11234这种情况时头节点为错认为1
