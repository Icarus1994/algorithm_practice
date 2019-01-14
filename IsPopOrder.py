# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        pushV.reverse()
        stack1 = pushV
        stack2 = []
        while popV:
            if stack2 and stack2[-1] == popV[0]:
                stack2.pop()
                popV.pop(0)
                continue
            if stack1:
                if stack1[-1] == popV[0]:
                    stack1.pop()
                    popV.pop(0)
                else:
                    stack2.append(stack1.pop())
            else:
                if stack2[-1] != popV[0]:
                    return False
        return True


result = Solution().IsPopOrder([1,2,3,4,5],[4,3,5,1,2])
print(result)

# 题目描述
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。

