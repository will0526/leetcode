# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s 由英文字母、数字、符号和空格组成 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 8055 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        occ = set()
        n = len(s)

        left, right, result = 0, 0, 0
        # 滑动窗口，右边出现的第一次重复肯定是左边第一个，左边滑动，
        # 如果没有，那右边继续滑动
        # 计算长度，右边减左边，如果比现在的长度大，更新
        # 直到到头，左边加结果大于长度，或者右边索引大于等于长度

        while left < n:
            if s[right] in occ:
                occ.remove(s[left])
                left += 1
            else:
                occ.add(s[right])
                right += 1

            if result < right - left:
                result = right - left
            if left + result >= len(s) or right >= len(s):
                break
        return result
# leetcode submit region end(Prohibit modification and deletion)
