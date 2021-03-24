"""
题目1：矩阵（面试）
题目2：200. 岛屿数量
题目3：695. 岛屿的最大面积
"""


"""
题目1：二维矩阵，值只有0，1.求孤立元素1的个数。孤立1指，值为1，且同行同列其余值全为0
面试考过，没有做出来，其实，你一步一步写出来，好好分析，是可以做出来的。哪怕是用复杂度最高的方式。
输入：
nums = [[0,1,0],
        [0,1,0],
        [1,0,0],
        [0,0,1]
       ]
输出2
"""
def fun(nums):
    m = len(nums)
    n = len(nums[0])
    cnt = 0
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 1: # 值为1
                flag_i = 0
                flag_j = 0
                for i2 in range(m): # 判断其余行值为0或1
                    if i2!=i and nums[i2][j]!=0:
                        flag_i = 1
                for j2 in range(n):
                    if j2!=j and nums[i][j2]!=0:# 判断其余列值为0或1
                        flag_j = 1
                if flag_i == 0 and flag_j==0: # 两个字段都为0，说明其余值为0，符合题目
                    cnt += 1
                    
    return cnt

"""
题目2：200. 岛屿数量
思路：
0  海洋格子
1  陆地格子（未遍历过）
2  陆地格子（已遍历）
注意：题解中这里修改了原数组，大家如果面试的时候，
要问清楚面试官是否能修改原数组，不能的话就得加入标记数组，
不要一给题就直接上手
"""
# 法一：dfs 遍历过的元素置'0'
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j]=='0':
                return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

# 法二：dfs 遍历过的元素置'2'
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j]=='0': # 边界条件，或不符合要求的条件
                return
            if grid[i][j] != '1': # 0 或 2
                return
            grid[i][j] = 2 # 遍历过置2
            dfs(grid, i-1, j) # 上
            dfs(grid, i+1, j) # 下
            dfs(grid, i, j-1) # 左
            dfs(grid, i, j+1) # 右
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(grid, i, j)
                    count += 1
        return count

# 法三：Bfs 遍历过的元素置'0'
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, i, j):
            queue = [[i,j]]
            while queue:
                [i,j] = queue.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]=='1':
                    grid[i][j] = '0'
                    queue += [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                bfs(grid, i, j)
                count += 1
        return count
# 法四：Bfs 遍历过的元素置'0'    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            queue = [(i, j)]
            grid[i][j] = '0'
            while queue:
                x, y = queue.pop(0)
                for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if a>=0 and a<m and b>=0 and b<n and grid[a][b]=='1':
                        queue.append((a, b))
                        grid[a][b] = '0'
        
        m = len(grid) # m 行
        n = len(grid[0]) # n 列
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)
        return res
# 法五：Bfs 遍历过的元素置'2'    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            if grid[i][j] == '0':
                return

            if grid[i][j] != '1':
                return

            queue = [(i, j)]
            grid[i][j] = '2'
            while queue:
                x, y = queue.pop(0)
                for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if a>=0 and a<m and b>=0 and b<n and grid[a][b]=='1':
                        queue.append((a, b))
                        grid[a][b] = '2'
        
        m = len(grid) # m 行
        n = len(grid[0]) # n 列
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)
        return res
                

"""
题目3：695. 岛屿的最大面积
思路：递归计算count
"""
# 法一：写法一
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, i, j):
            if not 0<= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j]==0:
                return 0
            count = 1 # 初始
            grid[i][j] = 0
            count += dfs(grid, i-1, j) # 记住形式
            count += dfs(grid, i+1, j)
            count += dfs(grid, i, j-1)
            count += dfs(grid, i, j+1)
            return count # 返回

        m = len(grid)
        n = len(grid[0])
        max_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = dfs(grid, i, j)
                    max_count = max(max_count, count)
        return max_count
# 法一：写法二
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if not 0<= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j]==0:
                return 0
            count = 1
            grid[i][j] = 0 # 如果值赋2,需要修改一些地方
            # count += dfs(grid, i-1, j)
            # count += dfs(grid, i+1, j)
            # count += dfs(grid, i, j-1)
            # count += dfs(grid, i, j+1)
            return count + dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1)

        m = len(grid)
        n = len(grid[0])
        max_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = dfs(grid, i, j)
                    max_count = max(max_count, count)
        return max_count
                

            
                    

            
        




