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

# 思路2 优化
# 添加一个辅助栈，特点是栈顶到栈底元素逐渐增大，栈顶元素即是当前原始栈最小值，元素之间相对顺序和元素在原始栈中的相对顺序相同
# 具体实现：当新添加的元素值小于等于辅助栈中栈顶元素（也就是辅助栈中最小元素）时，将新添加元素同时也压入辅助栈

instance.push(1)添加
instance.push(1)
