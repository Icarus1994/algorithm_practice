class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        low = head.next
        if low:
            fast = low.next
        else:
            return False
        while fast and fast.val != low.val:
            fast = fast.next
            if fast:
                fast = fast.next
            low = low.next
        return False if not fast else True


# 思路
# 假定链表头到环入口的距离是len，环入口到slow和fast交汇点的距离为x，环的长度为R。
# slow和fast第一次交汇时，设slow走的长度为：d = len + x，
# 而fast走的长度为：2d = len + nR + x，(n >= 1)，从而：即len = nR - x，(n >= 1)
# 因此声明两个指针a,b分别从链表头和fast low交汇处出发，a,b第一次相遇时的指针就是链表入口

# 注意
# 不同链表节点的值可以相同，因此判断有环时使用节点（对象）是否相等为判断条件
# 对象是否相等只的是内存地址是否相等，即指的是是否是同一对象。因为python中的赋值都是给对象添加引用，因此fast等指针变量指向的都是原来的链表节点

# 边界条件：
# 整个链表就是一个环；环大小为1；链表长度为1且整个链表是一个环
# 以上代码适用于这些边界
