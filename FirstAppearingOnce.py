# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.firstChar = "#"

    def FirstAppearingOnce(self):
        # write code here
        return self.firstChar

    def Insert(self, char):
        # write code here
        if not char:
            return
        dict = {}
        for i in range(len(char)):
            if char[i] in dict:
                dict[char[i]] = -1
            else:
                dict[char[i]] = i
        min = 100000
        for a in dict:
            if (dict[a] >= 0) and (dict[a] < min):
                min = dict[a]
                self.firstChar = a

str = "google"
res = Solution()
res.Insert(str)
print(res.FirstAppearingOnce())
