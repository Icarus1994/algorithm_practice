# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast = pHead
        low = pHead
        # 将fast和low在进入循环之前区分开。似乎只能这样，
        # 如果在while中加上fast low不为pHead的条件又不符合入口为pHead这种情况
        if not fast or not fast.next:
            return None
        fast = fast.next
        fast = fast.next
        low = low.next

        while not (fast is low):
            if not fast or not fast.next:
                return None
            fast = fast.next
            fast = fast.next
            low = low.next
            print("0")
        cross = low
        while not (cross is pHead):
            cross = cross.next
            pHead = pHead.next
            print("1")
        return cross

pHead = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
pHead.next = node1
node1.next = node2
node2.next = pHead
res = Solution().EntryNodeOfLoop(pHead)
print(res,pHead)


# 思路1
# fast和low指针一定会在环内相遇，因此fast一定比low多走了n个环，
# 又因为fast step=2,low step=1,环大小等于low step
# 将从头到第一次fast和low相遇的所有节点存入List，从1到n环大小进行循环，
# 每次判断low的下一个节点是否和list中某节点是同一个
# （这里利用了low指针在和fast相遇时是第一次进入环，即没有完整遍历完过一次环的特点），
# O（n2）

# 思路2 优化
# 假定链表头到环入口的距离是len，环入口到slow和fast交汇点的距离为x，环的长度为R。
# slow和fast第一次交汇时，设slow走的长度为：d = len + x，
# 而fast走的长度为：2d = len + nR + x，(n >= 1)，从而：即len = nR - x，(n >= 1)
# 因此声明两个指针a,b分别从链表头和fast low交汇处出发，a,b第一次相遇时的指针就是链表入口

# 边界条件：
# 整个链表就是一个环；环大小为1；链表长度为1且整个链表是一个环
