# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 104 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  Only one valid answer exists. 
#  
# 
#  
# Follow-up: Can you come up with an algorithm that is less than O(n2) time comp
# lexity? Related Topics 数组 哈希表 
#  👍 12182 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = dict()
        i = 0
        # 使用哈希表，将数作为key ，索引作为value 保存起来，通过差值去取索引，取到就返回。
        while i < len(nums):
            second = target - nums[i]
            sec_index = dict_nums.get(second)
            if sec_index is not None:
                return [sec_index, i]
            dict_nums[nums[i]] = i
            i = i + 1

        return None
# leetcode submit region end(Prohibit modification and deletion)
