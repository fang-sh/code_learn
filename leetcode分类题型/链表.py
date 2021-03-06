"""
题目1：21. 合并两个有序链表
题目2：23. 合并K个升序链表
题目3：148. 排序链表

"""


"""
题目1：21. 合并两个有序链表
参考：
https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
"""
# 迭代
def mergeTwoLists(l1, l2):
    head = ListNode(None)
    p = head
    while l1 and l2:
        if l1.val <= l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next # 进行下一步，此处容易漏掉
        
    head.next = l1 if not l2 else l2
    return p.next

# (掌握)递归
def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
"""  
题目2：23. 合并K个升序链表
"""



"""
题目3：148. 排序链表
思路：分割，归并排序
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 快慢指针，归并排序
        if not head or not head.next:
            return head 
        
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(tmp)
        return self.merge(left, right)

    # 合并两个有序链表
    def merge(self, left, right):
        res = ListNode(None)
        p = res
        while left and right:
            if left.val <= right.val:
                res.next = left
                left = left.next
            else:
                res.next = right
                right = right.next
            res = res.next
        res.next = left if not right else right
        return p.next
