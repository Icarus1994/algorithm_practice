# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minValue = None

    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.stack) ==1 :
            self.minValue = node
        else:
            if node < self.minValue:
                self.minValue = node

    def pop(self):
        # write code here
        if not self.stack:
            return
        popNode = self.stack.pop()
        if popNode == self.minValue:
            if self.stack:
                self.findMin()
            else:
                self.minValue = None
        return popNode

    def findMin(self):
        minValue = self.stack[0]
        for element in self.stack:
            if element < minValue:
                minValue = element
        self.minValue = minValue

    def top(self):
        # write code here
        if not self.stack:
            return
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minValue
instance = Solution()
instance.push(3)
instance.push(1)
instance.push(2)
instance.push(1)
instance.pop()
print(instance.min())


# 题目描述
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
