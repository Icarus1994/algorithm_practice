# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        arr = list(range(1,n+1))
        return sum(arr)

    def Sum_Solution1(self,n):
        return n and self.Sum_Solution1(n-1) + n

result = Solution().Sum_Solution1(1)
print(result)

# 解法一
# 使用python中sum()函数求可迭代对象中所有元素之和
# 解法二
# 题目要求不能用if和条件表达式，其考点是使用隐含的条件表达式and
# Python逻辑运算符and的含义是：a and b，如果a为false则返回a,a为真则返回b
