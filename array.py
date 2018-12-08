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

