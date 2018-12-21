# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif (n==1)|(n==2):
            return 1
        list = [0,1,1]
        for i in range(3,n+1):
            list.append(list[i-1] + list[i-2])
        return list.pop()

solu = Solution()
print(solu.Fibonacci(8))

# 题目描述
# 输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n <= 39