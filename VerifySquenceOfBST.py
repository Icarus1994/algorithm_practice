# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 1 or not sequence:
            return "true"
        root = sequence[-1]
        for i in range(0,len(sequence)-1):
            if sequence[i] >root:
                break

        leftTree = i
        if leftTree == len(sequence)-2:
            return self.VerifySquenceOfBST(sequence[0:-2])

        for j in range(i,len(sequence)-1):
            if sequence[j] < root:
                # print("execute for once")
                return "false"
        isLeftTree = self.VerifySquenceOfBST(sequence[0:leftTree])
        isRightTree = self.VerifySquenceOfBST(sequence[leftTree:-2])
        if (isLeftTree == "true") and (isRightTree == "true"):
            return "true"
        else:
            return "false"

print(Solution().VerifySquenceOfBST([7,4,6,5]))
