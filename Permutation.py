# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        result=[]
        if not ss:
            return []
        else:
            res = itertools.permutations(ss)
            for i in res:
                # 因为当有ss中有相同字母时，permutations方法认为它们是两个不同字母，实现全排列
                if "".join(i) not in result:
                    result.append("".join(i))
        return result
if __name__ == "__main__":
    str = "aAv"
    for i in itertools.permutations(str,3):
        print(i)
