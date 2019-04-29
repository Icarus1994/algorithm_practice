class Solution:
    def quick_sort(self,arr):
        if not arr or len(arr)==1:
            return arr
        return self.qsort(arr,0,len(arr)-1)

    def qsort(self,arr,left,right):
        key = arr[left]
        pl,pr = left,right
        # 该循环结束找到Key在arr中应有的位置
        while left< right:
            while left<right and arr[right]>=key:
                right-=1
            # 每次交换时都将key和另一个元素交换
            if left<right:
                t = arr[left]
                arr[left] = arr[right]
                arr[right] = t
            while left<right and arr[left]<=key:
                left+=1
            if left<right:
                t = arr[right]
                arr[right] = arr[left]
                arr[left] = t
        # 此时一定有left = right
        if pl < left-1:
            self.qsort(arr,pl,left-1)
        if pr > right +1:
            self.qsort(arr,right+1,pr)
        return arr
if __name__ == "__main__":
    arr = [9,3,2,1,4,6,7,0,5]
    ans = Solution().quick_sort([435,34])
    print(ans)

