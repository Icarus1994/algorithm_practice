# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        B = [self.productFromItoN(0,A)]
        tmp = 1
        for i in range(1,len(A)):
            tmp *= A[i-1]
            B.append(tmp * self.productFromItoN(i,A))
        return B

    def productFromItoN(self,i,arr):
        result = 1
        for j in range(i+1,len(arr)):
            result *= arr[j]
        return result

A = [1,2,3,4]
result = Solution().multiply([3])
print(result)