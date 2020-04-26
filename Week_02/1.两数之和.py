#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, num in enumerate(nums):
            if target - num in hash:
                return [hash[target-num],idx] 
            else:
                hash[num] = idx
    
# @lc code=end

