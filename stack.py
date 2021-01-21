'''
提目1：给定入栈顺序，判断出栈顺序是否合理

'''


# 题目1：给定入栈顺序，判断出栈顺序是否合理
# 题目描述：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
#    假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
#    但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
def is_right_order(pushV, popV):
    if len(pushV) == 0:
        return False
    stack = []
    for i in pushV:
        stack.append(i) #把元素压入栈中
        while stack and popV[0] == stack[-1]: # 判断条件
            stack.pop()
            popV.pop(0)
   
    if not stack: # 如果栈空，就返回True
        return True
    return False
