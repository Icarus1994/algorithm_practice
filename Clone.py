# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        newList = []
        randomNodeList = []
        oldNode = pHead
        while(oldNode):
            newList.append(RandomListNode(oldNode.label))
            randomNodeList.append(oldNode.random)
            oldNode = oldNode.next
        for i in range(0,len(newList)-1):
            newList[i].next = newList[i+1]
            newList[i].random = randomNodeList[i]
        newList[-1].random = randomNodeList[-1]
        return newList[0]
# 题目
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
# 另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（
# 注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

# 注意
# 复制链表新创建一个链表，这个链表所占内存大小等于原来链表的大小，链表中节点值和随机链接的节点要求和原来保持一致即可
# 考察python中赋值表示对对象的引用这一知识点
