# -*- coding: utf-8 -*-
#数据结构类型题：链表
#题目1-leecode-合并k个有序链表


#########################################################################

#题目1-leecode-合并k个有序链表
#题目描述：merge k个有序链表，结果按照顺序，以链表形式输出
#输入描述：
#    Input:{
#        1->4->5,
#        1->3->4,
#        2->6
#            }
#输出描述：1->1->2->3->4->5->6
#思路：用最小堆的方式，每次pop出最小的值，即堆顶元素，构造成链表形式，输出
import heapq
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        
class Solution:
    def mergekList(self, lists[ListNode])->ListNode:
        h = [] #最小堆minheap
        
        #将链表中所有元素，放到list h中
        for head in lists:#链表形式，每个链表只提供头结点，剩下的元素需通过next输出
                          #因此，链表的list中的元素，都是头结点一个元素
            node = head
            while node: #只要node不为空
                h.append(node.val)
                #或者h.append(node)
                node = node.next
        
        if not h: #忽略了[ [] ]的形式
            return None
        
        heapq.heapify(h)#将列表h构造成最小堆minheapq
        
        #构造链表，题目中要求以链表形式输出,注意为ListNode形式
        root = ListNode(heapq.heappop(h)) #将堆顶根元素输出
        curnode = root #指向头结点
        
        while h:
            nextnode = ListNode(heapq.heappop(h))
            curnode.next = nextnode
            curnode = nextnode
        return root #返回头结点即可
                
            












