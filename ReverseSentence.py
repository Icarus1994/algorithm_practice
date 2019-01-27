# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return s
        s = s + " "
        tmp = ""
        result = ""
        for a in s:
            if a == ' ':
                result = tmp + " " +result
                tmp = ""
            else:
                tmp = tmp + a
        return result[:-1]

s = "i am a stu."
result = Solution().ReverseSentence("a")
print(result)