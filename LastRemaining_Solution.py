# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n ==1:
            return 0
        elif n<=0 or m<=0:
            return -1
        stack = list(range(n))
        p = 0
        while len(stack) > 1:
            print("stack:", stack)
            if m > len(stack):
                length = len(stack)
                tmp = m % length
                while tmp > length:
                    tmp = tmp % length
                out = (p+tmp-1)%length
                stack.pop(out)
                # 原来位于out的数已经弹出，现在索引是Out的数就是原来的下一个数
                p = out
            else:
                out = (p+m-1)%len(stack)
                stack.pop(out)
                p = out
        return stack[0]
stack = list(range(4))
result= Solution().LastRemaining_Solution(5,3)
print(result)