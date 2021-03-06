"""
(1) 贪心算法之区间调度问题: https://mp.weixin.qq.com/s/NH8GFMcRm5UK0HmVhdNjMQ
        题目1：435. 无重叠区间
        题目2：452. 用最少数量的箭引爆气球

(2) 经典贪心算法：跳跃游戏: https://mp.weixin.qq.com/s/hMrwcLn01BpFzBlsvGE2oQ
        题目1：55. 跳跃游戏
        题目2：45. 跳跃游戏 II
        
(n)
        题目1：455. 分发饼干
"""
------------------------（1）-------------------------------



------------------------（2）-------------------------------
"""
题目1：55. 跳跃游戏

思路：尽可能到达最远位置（贪心）。
如果能到达某个位置，那一定能到达它前面的所有位置。

方法：初始化最远位置为 0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。
复杂度：时间复杂度 O(n)O(n)，空间复杂度 O(1)O(1)。

作者：mo-lan-4
链接：https://leetcode-cn.com/problems/jump-game/solution/pythonji-bai-97kan-bu-dong-ni-chui-wo-by-mo-lan-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
def canJump(nums):
    max_jump = 0 # 最大跳跃距离
    for i in range(len(nums)):
        jump = nums[i] #i为当前位置，jump是当前位置的跳数
        if max_jump >= i:
           max_jump = max(max_jump, i + jump)
    return max_jump >= i

------------------------（n）-------------------------------

"""
题目1：455. 分发饼干
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s = sorted(s)
        g = sorted(g)
        length = len(g)
        child = 0
        for i in s:
            if child < length and i >= g[child]:
                child += 1
            if child >= length:
                break
        return child

