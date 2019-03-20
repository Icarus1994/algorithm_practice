# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.minHeap,self.maxHeap = [0],[0]

    def Insert(self, num):
        self.minHeapInsert(num)
        # 必须要先将最小堆的堆顶插入到最大堆中，然后再判断最大堆的长度是否太长
        # 不能图省事，每次只判断最小堆的长度是否大于最大堆，
        # 否则最大堆和最小堆无法时刻保持分别存储了前一半小的数和后面一半大的数
        # 证明通过先实验加几个数，然后在该条件下用递归证明（数学归纳法）
        self.maxHeapInsert(self.minHeapPop())
        print("111",self.maxHeap,self.minHeap)
        if len(self.maxHeap) > len(self.minHeap):
            self.minHeapInsert(self.maxHeapPop())

    def GetMedian(self,n = None):
        # write code here
        if len(self.minHeap) == 1:
            return None
        elif len(self.minHeap) == len(self.maxHeap):
            return (self.maxHeap[1] + self.minHeap[1])/2
        else:
            return self.minHeap[1]

    def minHeapInsert(self,num):
        self.minHeap.append(num)
        i = len(self.minHeap)-1
        while i > 1 and self.minHeap[i//2] > num:
            self.minHeap[i] = self.minHeap[i//2]
            i //= 2
        self.minHeap[i] = num
        print("1",self.minHeap)

    def maxHeapInsert(self,num):
        self.maxHeap.append(num)
        i = len(self.maxHeap) - 1
        while i > 1 and self.maxHeap[i // 2] < num:
            self.maxHeap[i] = self.maxHeap[i // 2]
            i //= 2
        self.maxHeap[i] = num
        print("3",self.maxHeap)

    # pop时第一步弹出堆顶不能直接使用list.pop(1),因为pop(i)的复杂度为pop(k),最坏为O(n),
    # 这样比使用堆来找中位数的复杂度O(logn)都要大了
    def minHeapPop(self):
        res = self.minHeap[1]
        self.minHeap[1] = self.minHeap[-1]
        self.minHeap.pop()
        if len(self.minHeap) == 1:
            return res
        tmp = self.minHeap[1]
        i = 1
        while i <= (len(self.minHeap)-1)//2 and self.minHeap[2*i] < tmp:
            self.minHeap[i] = self.minHeap[2*i]
            i *= 2
        self.minHeap[i] = tmp
        print("2",self.minHeap)
        return res

    def maxHeapPop(self):
        res = self.maxHeap[1]
        self.maxHeap[1] = self.maxHeap[-1]
        self.maxHeap.pop()
        if len(self.minHeap) == 1:
            return res
        tmp = self.maxHeap[1]
        i = 1
        while i <= (len(self.maxHeap)-1)//2 and self.maxHeap[2*i] > tmp:
            self.maxHeap[i] = self.maxHeap[2*i]
            i *= 2
        self.maxHeap[i] = tmp
        return res

res = Solution()
# res.Insert(5)
# res.Insert(2)
# res.Insert(3)
# res.Insert(4)
# res.Insert(1)
# res.Insert(6)
# print(res.GetMedian())
# res.Insert(7)
# res.Insert(0)
# res.Insert(8)
# print(res.GetMedian())

# 整个逻辑没问题，单独测试4个堆函数哪里有问题

# 思路1 否定
# 本来想借助二分查找思想将字符流中的数字num插入到有序数组中并使其同样成为有序数组
# 发现插入num时用到list.insert方法，复杂度为O(n)导致整体复杂度为O(nlogn),遂采用简单方法

# 思路2
# 每次插入一个数字时就执行list.sort,输入n个数字insert方法的复杂度O(n^2logn)
# getmedian复杂度O(1)

# 思路3
# insert方法中构建最小堆，复杂度O(nlogn)
# getmedian复杂度O(nlogn),弹出n/2次，每次O(logn)

# 思路3 实现 自己的算法：
# insert时插入已有最下堆中，getMedian时从最小堆中弹出第n/2小的值
# 这样的问题是题目中如果insert，getMedian，insert,getMedian就会因为把之前的值丢掉出错。
# 而且题目还真是每inserst一次就getMedian一次

# 思路3 实现2 手写最大堆最小堆算法

# 思路3 实现3 利用heapq模块
# 见getMedian模块

