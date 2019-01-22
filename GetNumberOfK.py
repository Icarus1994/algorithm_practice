# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        left = 0
        right = len(data)-1
        cnt = 0
        while left <= right:
            mid = int((left + right)/2)
            if data[mid] > k:
                right = mid - 1
            elif data[mid] < k:
                left = mid + 1
            else:
                i = mid
                while (i <= len(data)-1) and data[i] == k:
                    cnt += 1
                    i += 1
                i = mid - 1
                while i >= 0 and data[i] == k:
                    cnt += 1
                    i -= 1
                break
        return cnt

arr = [1,2,3,3,3,3,4,5]
result = Solution().GetNumberOfK(arr,3)
print(result)

# 思路
# 将排序好的数组视为二叉搜索树
# 注意修改边界left和right时要在原来mid的基础上加减1，否则陷入死循环
