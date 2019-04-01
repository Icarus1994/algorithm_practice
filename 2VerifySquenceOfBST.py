# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 1 or not sequence:
            return True
        root = sequence[-1]
        for i in range(0,len(sequence)-1):
            if sequence[i] >root:
                break

        leftTree = i
        if leftTree == len(sequence)-2:
            return self.VerifySquenceOfBST(sequence[0:-2])

        for j in range(i,len(sequence)-1):
            if sequence[j] < root:
                return False
        return self.VerifySquenceOfBST(sequence[0:leftTree]) and self.VerifySquenceOfBST(sequence[leftTree:-2])


print(Solution().VerifySquenceOfBST([7,4,6,5]))
