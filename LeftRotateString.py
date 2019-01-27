# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if n < 0 or (not s) or (len(s) == 1):
            return s
        while n:
            letter = s[0]
            s = s[1:] + letter
            n -= 1
        return s

s = "abcde"
rol = Solution().LeftRotateString("d",1)
print(rol)
