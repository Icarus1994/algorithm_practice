# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 2:
            return []
        # d表示将tsum分为d个数之和，p为分为d个数之和时d个数的平均数，也起到指针的作用
        arr = []
        d = 2
        p = int(tsum/d)
        # p>0和i的起始范围从p-d算起，都是通过将搜索范围加宽，保证不遗漏可能的序列和，而且计算较简单
        while p > 0:
            # i是数组的起始位置
            for i in range(max(p - d,1),p+1):
                subArr = []
                sum  = 0
                for j in range(d):
                    subArr.append(i + j)
                    sum += i + j
                if sum == tsum:
                    arr.insert(0,subArr)
                    break
            d += 1
            p = int(tsum/d)
        return arr
print(Solution().FindContinuousSequence(15))