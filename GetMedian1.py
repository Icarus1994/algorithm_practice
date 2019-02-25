# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def __init__(self):
        self.heaps = [], []

    def Insert(self, num):
        # write code here
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def GetMedian(self,ss):
        # write code here
        small,large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0])/2
# 思路3 构造一个最大堆一个最小堆
# 最大堆存的是前1/2较小的数，最小堆存的是后1/2的较大的数
# 从堆中插入或删除元素复杂度O（logn）
# 每次有新元素时将元素添加置保持两个堆大小相差小于等于1
# 因为内置的headq模块只能生成最小堆，所以在保存前1/2较小的数时可以将每个数*（-1）保存到最小堆中