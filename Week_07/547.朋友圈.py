#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        father = [i for i in range(len(M))]
        def find(a):
            if father[a] != a:
                father[a] = find(father[a])
            return father[a]
        def union(a, b):
            father[find(b)] = find(a)
            return find(b)
        for i in range(len(M)):
            for j in range(i):
                if M[i][j]:
                    union(i, j)
        for i in range(len(M)):
            find(i)
        return len(set(father))
        
# @lc code=end

