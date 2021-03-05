"""
(1) LeetCode 股票问题的一种通用解法: https://mp.weixin.qq.com/s/TrN7mMdLEPCmT5mOXzgP5A
        时间复杂度高，不能通过所有题目，会超时，（2）中 动态规划法 优化
(2) 团灭 LeetCode 股票买卖问题: https://mp.weixin.qq.com/s/lQEj_K1lUY83QtIzqTikGA
        题目1：121. 买卖股票的最佳时机
        题目2：122. 买卖股票的最佳时机 II
        题目3：123. 买卖股票的最佳时机 III
        题目4：309. 最佳买卖股票时机含冷冻期
        题目5：714. 买卖股票的最佳时机含手续费
        题目6：188. 买卖股票的最佳时机 IV
        
"""

"""
题目1：121. 买卖股票的最佳时机
"""
# 法一
def maxProfit(prices):
    res = 0 # 记录最大利润
    curMin = prices[0] # 记录当前最小价格
    for i in prices:
        res = max(res, i-curMin) # 更新最大利润
        curMin = min(curMin, i) # 更新当前最小价格
    return res



"""
题目6：188. 买卖股票的最佳时机 IV
"""




