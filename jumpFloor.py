# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        k = number/2 + 1
        sum = 0
        for i in range(int(k)):
            sum += self.combinations(number-i,i)
        return sum

    def combinations(self,n,k):
        deno = 1
        for i in range(n-k+1,n+1):
            deno *= i
        return int(deno/self.jieCheng(k))

    def jieCheng(self,n):
        outcome = 1
        for i in range(1,n+1):
            outcome *= i
        return outcome

solu = Solution()
print(solu.jumpFloor(4))
# print(solu.jieCheng(1),solu.combinations (1,1))


# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）

# 解题思路
# 排列组合问题，解题分为两步，第一步确定跳n级台阶时跳a次2步，b次1步
# 第二步，跳a次2步时有C(a+b),a种跳法
# a的所有可能值为[0,num/2]
# 注：第一次想使用python标准库combinations函数实现，但是估计是导入库占了很大内存，导致内存超过限制

