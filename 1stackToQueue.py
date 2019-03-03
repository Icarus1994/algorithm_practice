# -*- coding:utf-8 -*-
class Solution:
    stack1 = []
    stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        # 最节省空间的方法,因为stack1和stack2中没有任何重复的数字
        if len(self.stack2) != 0:
            return self.stack2.pop()
        elif len(self.stack1) !=0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


# 题目描述
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# python是用list为基础实现队列和堆栈的
# 该问题卡在不知道题目给出的两个堆栈在哪里放进来
# 实际上，不会先给两个已初始化的堆栈和队列，只会通过队列的push和pop方法实现队列在不同时候的变化
