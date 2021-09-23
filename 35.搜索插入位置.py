#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left =0
        right = length-1
        while(left<=right):
            mid = int((left+right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid +1
            else:
                right = mid-1
        
        return left





