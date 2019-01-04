# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        #注意这里not的优先级高于or
        if not pHead or not pHead.next:
            return pHead
        list = []
        node = pHead
        while node != None:
            list.append(node)
            node = node.next
        # list != None和list!=[]是有区别的，前者会报错list index out of range
        list[0].next = None
        for i in range(1,len(list)):
            list[i].next = list[i-1]
        return list[-1]

# 题目描述
# 输入一个链表，反转链表后，输出新链表的表头

# 重新创建了一个List，不是最优解，参照python解答，带重构