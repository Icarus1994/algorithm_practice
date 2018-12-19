class Solution:
    def Find(self, target, array):
        if array == None:
            return False

        nrow = len(array)
        ncol = len(array[0])

        row = 0
        col = ncol-1
        while (row<nrow)&(col>=0):
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                row +=1
            else:
                col -=1
        return False


ls = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
t =7
ls1 = [[]]
solu = Solution()
print(solu.Find(t,ls1))


# 题目描述
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
