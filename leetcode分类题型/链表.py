"""
题目1：21. 合并两个有序链表
题目2：23. 合并K个升序链表
题目3：148. 排序链表
题目4：24. 两两交换链表中的节点

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


"""
题目4：24. 两两交换链表中的节点
"""
# (推荐)法一：递归
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

# （推荐）法二：理解原理   
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = ListNode(0, head)
        tmp = p 
        while tmp.next and tmp.next.next:
            node1 = tmp.next
            node2 = tmp.next.next
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = node1
        return p.next  
    
    