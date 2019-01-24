# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        # 解法1
        # 是否考虑非递减序列
        # 是否考虑tsum为0,array第一个元素为0且只有一个等于0的元素的情况
        # 由于element in list的平均复杂度为O(n),因此总的时间复杂度为O(n2)
        if not array or len(array) == 1:
            return []
        for i in array:
            if tsum - i in array:
                return [i, tsum - i]
        return []
arr = [1,2,3]
print(Solution().FindNumbersWithSum([2,3],3))

# 解法2
# 设置left=0,right=len(arr)-1两个指针，根据arr[left]+arr[right]结果缩小指针范围，试一下复杂度会不会降低