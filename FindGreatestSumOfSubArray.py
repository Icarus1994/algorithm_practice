# -*- coding:utf-8 -*-
class Solution:
    # 解法1
    # 递归，每个序列的最大连续子列和等于max(左子列的最大连续子列和,右子列的最大连续子列和，
    # 跨越左右分界线的最大连续子列和）
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        elif len(array) == 1:
            return array[0]
        length = int(len(array)/2)
        left = self.FindGreatestSumOfSubArray(array[:length])
        right = self.FindGreatestSumOfSubArray(array[length:])
        cross = self.FindGreatestSumInCross(array)
        return max(left,right,cross)

    def FindGreatestSumInCross(self,arr):
        left = int(len(arr)/2-1)
        right = left + 1

        max = 0
        if left:
            i = left-1
            sum = 0
            while i >=0:
                sum += arr[i]
                if sum > max:
                    max = sum
                i -= 1
        result = max + arr[left] + arr[right]

        max = 0
        if right < len(arr)-1:
            i = right+1
            sum = 0
            while i <= len(arr)-1:
                sum += arr[i]
                if sum > max:
                    max = sum
                i +=1
        result += max
        return result
    # 参考陈越
    def FindGreatestSumOfSubArray2(self,array):
        return
arr = [-2,-1]
print(Solution().FindGreatestSumOfSubArray(arr))