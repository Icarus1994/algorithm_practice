# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or (k <= 0) or (k > len(tinput)):
            return []
        # 类似冒泡排序法，只将前k个数冒到数组前面
        for i in range(0, k):
            m = i
            for j in range(i,len(tinput)):
                if tinput[j] < tinput[m]:
                    m = j
            tmp = tinput[i]
            tinput[i] = tinput[m]
            tinput[m] = tmp
        return tinput[:k]

arr = [4,5,1,6,2,7,3,8]
arr1 = [4]
print(Solution().GetLeastNumbers_Solution(arr,1))